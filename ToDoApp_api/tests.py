import os
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from ToDoApp_api.models import UserProfile, Task
from ToDoApp_api.serializers import UserProfileSerializer, TaskSerializer


class UserProfileViewSetTestCase(APITestCase):
    """Test case for UserProfileViewSet"""

    def setUp(self):
        """Set up initial data for each test"""
        self.client = APIClient()
        self.user = UserProfile.objects.create_user(
            name='testname',
            surname='testsurname',
            email='test@example.com',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)


    def test_retrieve_profile(self):
        """Test retrieving profile according to id"""
        url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = UserProfileSerializer(instance=self.user)
        self.assertEqual(response.data, serializer.data)

    def test_create_profile(self):
        """Test creating profile"""
        url = reverse('profile-list')
        data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john@example.com',
            'password': 'somepassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the profile is actually created in the database
        profile_exists = UserProfile.objects.filter(
            name='John',
            surname='Doe',
            email='john@example.com'
        ).exists()
        self.assertTrue(profile_exists, "Profile should have been created in the database.")


    def test_delete_profile(self):
        # Delete the profile
        url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Ensure successful deletion

        # Check if the profile no longer exists
        retrieve_url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        retrieve_response = self.client.get(retrieve_url)
        self.assertEqual(retrieve_response.status_code, status.HTTP_404_NOT_FOUND)  # Ensure profile is not found

    def test_update_profile(self):
        """
        Test updating a user profile.
        """

        # Make PUT request to update the profile
        url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        data = {
            'name': 'Updated Name',
            'surname': 'Updated Surname',
            'email': 'updated_email@example.com',
            'password': 'newpassword'
        }
        response = self.client.put(url, data)

        # Check if the response status code is as expected
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the profile is updated in the database
        updated_profile = UserProfile.objects.get(pk=self.user.pk)
        self.assertEqual(updated_profile.name, 'Updated Name')
        self.assertEqual(updated_profile.surname, 'Updated Surname')
        self.assertEqual(updated_profile.email, 'updated_email@example.com')


    def test_partial_update_profile(self):
        """Test partially updating a user profile."""


        # Make PATCH request to partially update the profile
        url = reverse('profile-detail', kwargs={'pk': self.user.pk})
        data = {
            'name': 'Updated Name',
            'surname': 'Updated Surname',
        }
        response = self.client.patch(url, data)

        # Check if the response status code is as expected
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the profile is partially updated in the database
        updated_profile = UserProfile.objects.get(pk=self.user.pk)
        self.assertEqual(updated_profile.name, 'Updated Name')
        self.assertEqual(updated_profile.surname, 'Updated Surname')
        # Ensure that other fields remain unchanged
        self.assertEqual(updated_profile.email, 'test@example.com')


class TaskViewSetTestCase(APITestCase):
    """Test case for UserProfileViewSet"""

    def setUp(self):
        """Set up initial data for each test"""
        self.client = APIClient()
        self.user = UserProfile.objects.create_user(
            name='testname',
            surname='testsurname',
            email='test@example.com',
            password='password123'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        """Test creating a new task"""
        url = reverse('task-list')
        data = {
            'title': 'Test task',
            'description': 'Test task description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
