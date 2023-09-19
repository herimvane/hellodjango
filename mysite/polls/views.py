from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from .models import Question,Choice

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_question(request):
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    return HttpResponse('Success!')


def month_archive(request, year,month):
    return HttpResponse(year+month)
