


from my_app.models import Question,Choice
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Hello')

def question_list(request):
    context={}
    context["details"]=Question.objects.all()
    return render(request,"questions.html",context)

def choose(request,id):
     context={}
     context["details"]=Choice.objects.filter(choose=id)
     return render(request,"choices.html",context)
    