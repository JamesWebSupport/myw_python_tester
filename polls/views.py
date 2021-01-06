from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("You are in the Poll Page")

def detail(request, question_id):
    response = "The Question is %s"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = "Results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "Vote on the question %s"
    return HttpResponse(response % question_id)