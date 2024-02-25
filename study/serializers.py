from rest_framework import serializers
from study.models import Course, Lesson
from rest_framework.relations import SlugRelatedField


class LessonSerializer(serializers.ModelSerializer):
    # SlugRelatedField для вывода названия курса, а не его id
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

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
