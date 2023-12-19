"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

SchemaView = get_schema_view(
    info=openapi.Info(
        title='Recording system',
        default_version='v1.0',
        description='This is a registration system for city clinics',
        terms_of_service='',
        contact=openapi.Contact(name='Seilbekov Darkhan', url='https://github.com/darkhan2409'),
        license=openapi.License(name='JustCode')
    ),
    patterns=[
        path('admin/', admin.site.urls),
        path('patient/', include('patient_app.urls')),
        path('clinic/', include('clinic_app.urls')),
        path('specialist/', include('specialist_app.urls')),
        path('review/', include('review_app.urls')),
        path('record/', include('record_app.urls')),
    ],
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/', include('patient_app.urls')),
    path('clinic/', include('clinic_app.urls')),
    path('specialist/', include('specialist_app.urls')),
    path('review/', include('review_app.urls')),
    path('record/', include('record_app.urls')),
    path('swagger/', SchemaView.with_ui()),
]
