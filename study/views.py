from study.models import Course, Lesson
from rest_framework.viewsets import ModelViewSet
from study.serializers import (CourseSerializer,
                               LessonSerializer, PaymentSerializer)
from rest_framework.generics import (RetrieveAPIView, ListAPIView,
                                     CreateAPIView, UpdateAPIView,
                                     DestroyAPIView)
from users.models import Payment
from rest_framework import filters


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class PaymentList(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['course__name', 'lesson__name', 'type']
