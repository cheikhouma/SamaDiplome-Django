from django.urls import path
from . import views


urlpatterns = [
    path('', views.ChangePassword.as_view(), name="securite"),
    path('<str:username>/', views.ChangePassword.as_view(), name="securite"),
]
