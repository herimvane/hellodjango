from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from .models import Question, Choice, Blog


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_question(request):
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    return HttpResponse('Success!')

def get_question(request):
    qs = Question.objects.all() # 查询所有Question
    # q = Question.objects.get(id=1) # 查询id=1的Question
    # q = Question.objects.filter(id=1) # 过滤
    # q = Question.objects.filter(question_text__startswith="What") # 过滤以What开头
    # __表示为属性
    # q = Question.objects.get(pub_date__year=current_year) # 查询pub_date为今年的
    q = Question.objects.get(pk=1)  # 查询主键值为1的Question

    # 为q添加三个choice
    # a = q.choice_set.create(choice_text="Not much", votes=0)
    # b = q.choice_set.create(choice_text="The sky", votes=0)
    # c = q.choice_set.create(choice_text="Just hacking again", votes=0)

    cs = q.choice_set.all()  # 查询与q关联的所有Choice
    count = q.choice_set.count() # 统计与q关联的Choice数量
    current_year = timezone.now().year
    cs2 = Choice.objects.filter(question__pub_date__year=current_year) # 查询与pub_date为今年的Question关联的所有Choice
    c = q.choice_set.filter(choice_text__startswith="Just hacking") # 查询与q关联的且以Just hacking开头的Choice

    c.delete()  # 删除c
    print(Blog.objects.with_counts()[0].num_entry)
    return HttpResponse('Success!')

def month_archive(request, year,month):
    return HttpResponse(year+month)
