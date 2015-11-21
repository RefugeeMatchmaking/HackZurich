from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import User

def index(request):
    users = User.objects.all()[:5]
    template = loader.get_template('lighthouse/index.html')
    context = RequestContext(request, {'users': users,}) 
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "Result of question %s."
    return HttpResponse(response % question_id)

