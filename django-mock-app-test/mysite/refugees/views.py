# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. This is index")

def refugee(request, question_id):
    return HttpResponse("Blah Blah Blah")
