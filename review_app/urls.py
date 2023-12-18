from .views import *
from django.urls import path


urlpatterns = [
    path('create/', ReviewCreateApiView.as_view()),
    path('delete/<int:review_id>/', ReviewDeleteApiView.as_view())
]
