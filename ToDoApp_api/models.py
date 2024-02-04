from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, surname, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Please provide an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, surname, password):
        """Create a new superuser"""
        user = self.create_user(email, name, surname, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user
class TaskManager(models.Manager):
    """Manager for tasks"""

    def create_task(self, user,user_email, title, description, completed):
        task = self.model(user=user,user_email=user_email, title=title, description=description, completed=completed)
        task.save(using=self.db)

        return task

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def get_full_name(self):
        """Retrieve full name of user"""
        return f'{self.name} {self.surname}'

    def get_short_name(self):
        """"Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Task(models.Model):
    """Model for tasks"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    objects = TaskManager()

    def save(self, *args, **kwargs):
        # Automatically populate the email field based on the associated user's email
        if not self.email and self.user:
            self.email = self.user.email

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title