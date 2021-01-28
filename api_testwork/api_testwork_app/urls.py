from django.urls import path
from rest_framework import routers

from . import api


router = routers.DefaultRouter()
router.register('users', api.UserViewSet)
router.register('polls', api.PollList)
router.register('questions', api.QuestionsList)
router.register('choices', api.ChoiceList)
router.register('answers', api.AnswerList)
urlpatterns = router.urls

urlpatterns += [
    path('polls/active', api.active_polls_view, name='active_polls_view'),
    path('answers/view/<int:user_id>', api.answer_view, name='answer_view'),
]
