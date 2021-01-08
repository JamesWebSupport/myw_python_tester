# Create your views here.
from django.shortcuts import render

from polls.models import Question


from django.shortcuts import render

from polls.models import Question


def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)