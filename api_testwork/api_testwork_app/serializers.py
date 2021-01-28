from django.contrib.auth.models import User
from rest_framework import serializers
from api_testwork_app.models import Poll, Question, Choice, Answer


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_staff', 'username']

    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id


class AnswerSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=UserSerializers())
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)

    class Meta:
        model = Answer
        fields = ['id', 'user_id', 'poll', 'question', 'choice']

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).question_type
        try:
            if question_type == 'text' or question_type == 'one_choice':
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user_id=attrs['user_id'])
            elif question_type == 'multiple_choices':
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user_id=attrs['user_id'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Already responded')


class ChoiceSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=500)

    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text']

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, choice_text=attrs['choice_text'])
        except Choice.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Choice already exists')

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=500)
    question_type = serializers.CharField(max_length=500)
    choices = ChoiceSerializers(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'question_text', 'question_type', 'choices']

    def validate(self, attrs):
        question_type = attrs['question_type']
        if question_type == 'text' or question_type == 'one_choice' or question_type == 'multiple_choices':
            return attrs
        raise serializers.ValidationError('Question type can be only text_type, one_choice, multiple_choices,')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    poll_name = serializers.CharField(max_length=1000)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    poll_description = serializers.CharField(max_length=1000)
    questions = QuestionsSerializers(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'poll_name', 'start_date', 'end_date', 'poll_description', 'questions']

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'start_date': 'Wrong this field!'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
