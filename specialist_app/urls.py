from .views import *
from django.urls import path


urlpatterns = [
    path('', SpecialistsApiView.as_view()),
]
