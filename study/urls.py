from django.urls import path
from study.apps import StudyConfig
from rest_framework import routers
from study.views import *

app_name = StudyConfig.name


urlpatterns = [
    path('lesson/', LessonListView.as_view()),
    path('lesson/create/', LessonCreateView.as_view()),
    path('lesson/<int:pk>', LessonDetailView.as_view()),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view()),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view()),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns += router.urls
