from django.urls import path
from .views import (
    AnswerList,
    AnswerDetail,
    AnsweredQuestionList,
    AnsweredQuestionDetail,
)

urlpatterns = [
    path("", AnswerList.as_view(), name="answer_list"),
    path("<int:pk>/", AnswerDetail.as_view(), name="answer_detail"),
    path(
        "answered-questions/",
        AnsweredQuestionList.as_view(),
        name="answered_question_list",
    ),
    path(
        "answered-questions/<int:pk>/",
        AnsweredQuestionDetail.as_view(),
        name="answered_question_detail",
    ),
]
