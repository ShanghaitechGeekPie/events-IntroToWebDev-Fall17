from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Question, Choice

"""
从 tutorial part 1 来的
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""
从 tutorial part 3 来的
"""
def detail(request, q_id):
    q = Question.objects.get(pk=q_id)
    chs = Choice.objects.filter(question_id=q_id).values('choice_text')
    return JsonResponse(
        {
            "q": q.question_text,
            "chs": list(chs)
        }
    )

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)