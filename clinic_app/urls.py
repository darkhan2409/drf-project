from .views import *
from django.urls import path


urlpatterns = [
    path('', ClinicApiView.as_view()),
]
