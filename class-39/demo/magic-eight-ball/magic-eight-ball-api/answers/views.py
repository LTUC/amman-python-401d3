from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Answer, AnsweredQuestion
from .permissions import IsOwnerOrReadOnly
from .serializers import AnswerSerializer, AnsweredQuestionSerializer


class AnswerList(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnsweredQuestionList(ListCreateAPIView):
    queryset = AnsweredQuestion.objects.all()
    serializer_class = AnsweredQuestionSerializer


class AnsweredQuestionDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = AnsweredQuestion.objects.all()
    serializer_class = AnsweredQuestionSerializer
