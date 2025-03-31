from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackView.as_view()),
    path('<str:username>/', views.FeedbackView.as_view()),
    path('<int:id>/', views.FeedbackView.as_view())
]
