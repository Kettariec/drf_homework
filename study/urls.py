from django.urls import path
from study.apps import StudyConfig
from rest_framework import routers
from study.views import (LessonListView, LessonCreateView,
                         LessonDetailView, LessonUpdateView,
                         LessonDeleteView, CourseViewSet,
                         SubscriptionAPIView)

app_name = StudyConfig.name


urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lessons_list'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),

    path('subscription/', SubscriptionAPIView.as_view(), name='subscription')
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns += router.urls
