import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
    pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"],
[])
        
def test_past_question(self):
    question = create_question(question_text="Past question",days=30)
    response = self.client.get(reverse("polls:index"))
    self.assertQuerySetEqual(
        response.context["latest_question_list"],
        [question],
    )

def test_future_question(self):
    question = create_question(question_text="Future question",days=30)
    response = self.client.get(reverse("polls:index"))
    self.assertContains(response, "No polls are available.")
    self.assertQuerySetEqual(response.context["latest_question_list"],
[])

def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        
    
