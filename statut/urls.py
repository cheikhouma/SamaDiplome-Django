from django.urls import path
from . import views


urlpatterns = [
    path('', views.StatutView.as_view()),
    path('<str:username>/', views.StatutView.as_view()),
]
