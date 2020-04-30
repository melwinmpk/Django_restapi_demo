"""DemorestApi URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from updates.views import (
    json_example_view,
    JsonCBV,JsonCBV2,
    SerizlizedListView,
    SerizlizedDetailView
)

urlpatterns = [
    path('json/example',json_example_view, name=''),
    path('json/classexample1',JsonCBV.as_view(), name=''),
    path('json/classexample2',JsonCBV2.as_view(), name=''),
    path('json/serialized/list',SerizlizedListView.as_view(), name=''),
    path('json/serialized/detail',SerizlizedDetailView.as_view(), name=''),
    path('api/upadtes/',include('updates.api.urls')),
    path('api/status/',include('status.api.urls')),
    path('api/auth/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
