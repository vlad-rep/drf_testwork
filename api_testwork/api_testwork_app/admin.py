from django.contrib import admin
from api_testwork_app.models import Poll, Question, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    model = Poll
    list_display = ['id', 'poll_name','start_date','end_date']


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['id', 'get_poll', 'question_text', 'question_type']

    def get_poll(self, obj):
        return obj.poll.id

    get_poll.admin_order_field = 'poll'
    get_poll.short_description = 'Poll Name'


class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ['id', 'get_question', 'choice_text']

    def get_question(self, obj):
        return obj.question.id

    get_question.admin_order_field = 'question'
    get_question.admin_description = 'Question Text'


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ['id', 'user_id', 'get_poll', 'get_question', 'get_choice']

    def get_poll(self, obj):
        return obj.poll.id

    get_poll.admin_order_field = 'poll'
    get_poll.short_description = 'Poll Name'

    def get_question(self, obj):
        return obj.question.id

    get_question.admin_order_field = 'question'
    get_question.admin_description = 'Question Text'

    def get_choice(self, obj):
        return obj.choice.id

    get_choice.admin_order_field = 'choice'
    get_choice.admin_description = 'Choice Text'


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
