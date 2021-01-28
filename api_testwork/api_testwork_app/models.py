from django.db import models


class Poll(models.Model):
    poll_name = models.CharField(max_length=1000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    poll_description = models.CharField(max_length=1000)


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=500)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
