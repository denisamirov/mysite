from django.urls import path

from .views import index, by_class

urlpatterns = [
    path('', index),
    path('class/<str:class_id>/', by_class),
]