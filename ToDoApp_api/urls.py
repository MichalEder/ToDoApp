from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ToDoApp_api import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('task', views.TaskViewSet)


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]