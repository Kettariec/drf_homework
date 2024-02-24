from rest_framework import serializers
from study.models import Course, Lesson
from users.models import Payment, User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment_list = PaymentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
