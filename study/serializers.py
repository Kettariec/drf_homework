from rest_framework import serializers
from study.models import Course, Lesson, Subscription
from rest_framework.relations import SlugRelatedField
from study.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    # SlugRelatedField для вывода названия курса, а не его id
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)
    is_subscription = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_is_subscription(self, course):
        user = self.context['request'].user
        subscription = Subscription.objects.filter(course=course.id, user=user.id)
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
