from .views import *
from django.urls import path


urlpatterns = [
    path('sign_up/', SignUpApiView.as_view()),
    path('sign_in/', SignInApiView.as_view()),
    path('sign_out/', SignOutApiView.as_view()),

    path('profile/', ProfileApiView.as_view()),
]
