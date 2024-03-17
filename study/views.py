from study.models import Course, Lesson, Subscription
from rest_framework.viewsets import ModelViewSet
from study.serializers import CourseSerializer, LessonSerializer
from rest_framework.generics import (RetrieveAPIView, ListAPIView,
                                     CreateAPIView, UpdateAPIView,
                                     DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from study.permissions import IsModerator, IsOwner
from study.pagination import CourseAndLessonPagination
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from users.serializers import PaymentSerializer
from users.models import Payment
from study.services import StripeService
from config.settings import STRIPE_API


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CourseAndLessonPagination

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [~IsModerator, IsAuthenticated]
        elif self.action == 'retrieve' or 'list':
            permission_classes = [IsModerator | IsOwner]
        elif self.action == 'update' or 'partial_update':
            permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [~IsModerator, IsOwner]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = CourseAndLessonPagination


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDeleteView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        # get_or_create возвращает кортеж из двух элементов:
        # объект и bool(создан или получен из базы)
        subs_item, created = Subscription.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'подписка добавлена'
        else:
            subs_item.delete()
            message = 'подписка удалена'

        return Response(message)


class PayCourseAPIView(CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        course_pk = self.kwargs.get('pk')
        new_payment.paid_course = Course.objects.get(pk=course_pk)
        session = StripeService(STRIPE_API).create_payment(new_payment.paid_course,
                                                           new_payment.user)
        new_payment.session_id = session.id
        new_payment.payment_url = session.url
        new_payment.save()


class CheckPaymentAPIView(RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_object(self):
        self.object = super().get_object()
        session_id = self.object.session_id
        session = StripeService(STRIPE_API).check_payment(session_id)
        if session.payment_status == 'paid' or session.payment_status == 'complete':
            self.object.is_paid = True
        self.object.save()
        return self.object
