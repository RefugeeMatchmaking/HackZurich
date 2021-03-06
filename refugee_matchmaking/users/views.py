from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Max
from ipware.ip import get_ip
import sys

#Import database
from .models import User, Language
#Import Form
from .forms import UserForm

#Import Dataprocessing functions from algorithms folder
from users.algorithms.get_square_V2 import get_square
from users.algorithms.lat_long import lat_long

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        ip = get_ip(request)
        print('Valid Form', form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            #Set IP
            user.submission_ip = ip
            
            # temporarily here. Please move this to the form and 
            # check if lat/long data are available before saving
            
            lat, lon = lat_long(user.location)

            user.lat = lat
            user.lon = lon 

            user.save() #save user
            matchNewUser(pk=user.pk)
            return redirect('user_detail', pk=user.pk, permanent=True)
    else:
        form = UserForm()

    return render(request, 'users/index.html', {'form': form})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'users/user_detail.html', {'user': user})


#Functions to call the algorithms

def matchNewUser(pk):
    print('matchNewUser algorithm has been called')

    user= get_object_or_404(User, pk=pk)

    all_locals=User.objects.filter(refugee_or_local='L', matched=False, flag='N')
    all_refugees=User.objects.filter(refugee_or_local='R', matched=False, flag='N')

    if len(all_locals)>2 and len(all_refugees)>2: 
        #Dont run score if there arn't enough people in the database
        score=get_square(user, all_locals, all_refugees)
        matchedUsers=score[0]
        if matchedUsers:
            maxnumber=User.objects.all().aggregate(Max('groupnumber'))['groupnumber__max']
            newgroupnumer=maxnumber+1
            print('new group number is',newgroupnumer)

            for matchedUser in matchedUsers:
                matchedUser.matched=True

                matchedUser.groupnumber=newgroupnumer
                matchedUser.save()

        print('score is:', score)
    user=get_object_or_404(User, pk=pk)
