from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import *


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + timedelta(days=30)
        question = Question(date=time)

        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        question = Question(date=time)

        self.assertIs(question.was_published_recently(), True)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        question = Question(date=time)

        self.assertIs(question.was_published_recently(), True)


def create_question(text, days):
    time = timezone.now() + timedelta(days=days)

    return Question.objects.create(text=text, date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["questions"], [])

    def test_past_question(self):
        create_question(text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["questions"],
            ["<Question: Past question.>"]
        )

    def test_future_question(self):
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["questions"], [])

    def test_future_question_and_past_question(self):
        create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["questions"],
            ["<Question: Past question.>"]
        )

    def test_two_past_questions(self):
        create_question(text="Past question 1.", days=-30)
        create_question(text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["questions"],
            ["<Question: Past question 2.>", "<Question: Past question 1.>"]
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        question = create_question(text="Future question.", days=5)
        response = self.client.get(reverse("polls:detail", args=(question.id,)))

        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        question = create_question(text="Past Question.", days=-5)
        response = self.client.get(reverse("polls:detail", args=(question.id,)))

        self.assertContains(response, question.text)
