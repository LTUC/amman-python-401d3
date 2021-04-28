from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text


class AnsweredQuestion(models.Model):
    question = models.TextField()
    reply = models.TextField()

    def __str__(self):
        return self.question
