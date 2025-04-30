from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackView.as_view(), name="contact"),
    path('<str:username>/', views.FeedbackView.as_view(), name="contact"),
]
