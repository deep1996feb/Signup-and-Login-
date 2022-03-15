"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path, include
from api.views import RegisterationAPIView, UserInfoAPIView, UserDetail, RegistrationAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', RegisterationAPIView.as_view(), name='register'),
    path('auth/login', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('auth/userinfo', UserInfoAPIView.as_view(), name='info'),
    path('auth/info/<int:pk>', UserDetail.as_view(), name='detail'),
    path('auth/updatedlt/<int:pk>', RegistrationAPI.as_view(), name='updatedlt'),

]
