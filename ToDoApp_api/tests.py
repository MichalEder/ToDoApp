import os
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from ToDoApp_api.models import UserProfile
from ToDoApp_api.serializers import UserProfileSerializer


class UserProfileViewSetTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create_user(
            name='testname',
            surname='testsurname',
            email='test@example.com',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)


    def test_retrieve_profile(self):
        url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        serializer = UserProfileSerializer(instance=self.user)
        self.assertEqual(response.data, serializer.data)

    def test_create_profile(self):
        url = reverse('profile-list')
        data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john@example.com',
            'password': 'somepassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)