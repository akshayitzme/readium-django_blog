from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('articles/<int:id>', views.article)
]
