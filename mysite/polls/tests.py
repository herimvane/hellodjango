from django.test import TestCase
from django.utils import timezone

from .models import Question,Choice

class MyTest(TestCase):
    def setUp(self):
        Question.objects.create(question_text="What's new?", pub_date=timezone.now())

    def test_me(self):
        q = Question.objects.get(id=1)
        print(q.id)
