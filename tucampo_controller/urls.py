from django.urls import path, include
from rest_framework import routers
from tucampo_controller import views

router = routers.DefaultRouter()
router.register(r'create-user', views.CreateUser, basename='create-user')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
