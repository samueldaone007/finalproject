from django.urls import path
from .views import QuizAI

urlpatterns = [
    path('QuizAI', QuizAI, name='QuizAI'),
]
