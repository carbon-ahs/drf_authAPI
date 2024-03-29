from django.urls import path

from accounts.views import (
    UserChangePasswordView,
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
)


# from .views import say_hello

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("change-password/", UserChangePasswordView.as_view(), name="change_password"),
]
