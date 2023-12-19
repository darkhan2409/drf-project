from .views import *
from django.urls import path


urlpatterns = [
    path('my/', RecordApiView.as_view()),
    path('update/<int:record_id>/', RecordUpdateApiView.as_view()),
    path('delete/<int:record_id>/', RecordDeleteApiView.as_view()),
]
