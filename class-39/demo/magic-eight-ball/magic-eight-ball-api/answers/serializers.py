from rest_framework import serializers
from .models import Answer, AnsweredQuestion


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class AnsweredQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnsweredQuestion
        fields = "__all__"
