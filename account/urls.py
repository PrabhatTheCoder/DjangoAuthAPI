from django.contrib import admin
from django.urls import path, include
from .views import UserRegisttation, LoginUserView, UserProfileView, UserPasswordChange, SendPasswordResetEmailView, UserPasswordResetView


urlpatterns = [
    path('registration/', UserRegisttation.as_view()),
    path('login/', LoginUserView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('password-change/', UserPasswordChange.as_view()),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view()),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view()),
]
