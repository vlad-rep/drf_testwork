from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api_testwork_app.models import Poll, Question, Choice, Answer
from api_testwork_app.serializers import UserSerializers, PollSerializers, QuestionsSerializers, ChoiceSerializers, \
    AnswerSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class PollList(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers


class QuestionsList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializers


class ChoiceList(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializers


class AnswerList(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def active_polls_view(request):
    polls = Poll.objects.filter(end_date__gte=timezone.now())
    serializer = PollSerializers(polls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def answer_view(request, user_id):
    answers = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializers(answers, many=True)
    return Response(serializer.data)
