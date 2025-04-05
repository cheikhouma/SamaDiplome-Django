from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChangePassword.as_view()),
    path('<str:username>/', views.ChangePassword.as_view()),
]
