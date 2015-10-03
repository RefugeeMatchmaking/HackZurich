from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from ipware.ip import get_ip
from .models import User, Language
from .forms import UserForm

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        ip = get_ip(request)
        if form.is_valid():
            user = form.save(commit=False)
            user.submission_ip = ip
            user.save()
            return redirect('user_detail', pk=user.pk, permanent=True)
    else:
        form = UserForm()

    return render(request, 'users/index.html', {'form': form})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'users/user_detail.html', {'user': user})