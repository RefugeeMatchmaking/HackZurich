from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from ipware.ip import get_ip
import sys

#extend python path at runtime
#sys.path.append('./algorithms') #Doesn't really work...


from .models import User, Language
from .forms import UserForm
#from get_square import *
from users.algorithms.get_square import * #Throws an error as get_square.py can't import other files


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        ip = get_ip(request)
        print('Valid Form', form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            #Set IP
            user.submission_ip = ip
            

            user.save()
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
    print('hello new user')
    #u=User.objects.get(pk=pk)
    user= get_object_or_404(User, pk=pk)
    print('type',user.location)

    all_locals=User.objects.filter(refugee_or_local='L')
    all_refugees=User.objects.filter(refugee_or_local='R')

    #get_square(user, all_locals, all_refugees)