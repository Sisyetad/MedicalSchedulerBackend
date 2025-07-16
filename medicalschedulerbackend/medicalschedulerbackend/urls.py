"""
URL configuration for medicalschedullerbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# medicalschedulerbackend/urls.py (root project urls.py)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('headoffice/', include('Admin.urls')),
    path('api/v1/auth/', include('User.auth_urls')),
    path('api/v1/users/', include('User.urls')),
    path('api/v1/roles/', include('Role.urls')),
    path('api/v1/branches/', include('Branch.urls')),
    path('api/v1/doctors/', include('Doctor.urls')),
    path('api/v1/receptionists/', include('Receptionist.urls')),
    path('api/v1/patients/', include('Patient.urls')),
    path('api/v1/queues/', include('Queue.urls')),
    path('api/v1/diagnosis/', include('Diagnosis.urls'))
]
