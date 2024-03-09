from rest_framework.test import APITestCase, APIClient
from users.models import User
from study.models import Lesson, Course, Subscription
from django.urls import reverse
from rest_framework import status


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='test', owner=self.user)
        self.lesson = Lesson.objects.create(name='test', course=self.course,
                                            video='https://www.youtube.com/123',
                                            owner=self.user)

    def test_list_lessons(self):
        response = self.client.get(
            reverse('study:lessons_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 4, 'course': 'test', 'name': 'test',
                          'description': None, 'image': None,
                          'video': 'https://www.youtube.com/123', 'owner': 3}]}
        )

    def test_create_lesson(self):
        data = {
            "name": "test",
            "course": "test",
            "video": "https://www.youtube.com/123"
        }
        response = self.client.post(reverse('study:lesson_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         {'id': 2, 'course': 'test', 'name': 'test',
                          'description': None, 'image': None,
                          'video': 'https://www.youtube.com/123', 'owner': 1})

    def test_retrieve_lesson(self):
        response = self.client.get(
            reverse('study:lesson', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {'id': 5, 'course': 'test', 'name': 'test',
                          'description': None, 'image': None,
                          'video': 'https://www.youtube.com/123', 'owner': 4})

    def test_update_lesson(self):
        data = {
            "name": "test",
            "course": "test",
            "video": "https://www.youtube.com/123"
        }
        response = self.client.patch(
            reverse('study:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'course': 'test', 'name': 'test',
             'description': None, 'image': None,
             'video': 'https://www.youtube.com/123', 'owner': 5}
        )

    def test_delete_lesson(self):
        response = self.client.delete(
            reverse('study:lesson_delete', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name="test", owner=self.user)
        self.subscription = Subscription.objects.create(course=self.course, user=self.user)

    def test_create_subscription(self):
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }

        response = self.client.post(reverse('study:subscription'), data=data)
        print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'подписка добавлена'}
        )
