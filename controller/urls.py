from django.urls import path, include
from rest_framework import routers
from controller import views

router = routers.DefaultRouter()
router.register(r'create-user', views.CreateUser, basename='create-user') #La url es create-user/api/v1/create-user

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
