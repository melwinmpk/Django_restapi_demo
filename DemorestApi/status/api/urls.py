# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from .views import (
    StatusListSearchAPIView,
    StatusAPIView,
    StatusCreateAPIView,
    StatusDetailAPIView,
    StatusUpdateAPIView,
    StatusDeleteAPIView
)
urlpatterns =[
    path('', StatusAPIView.as_view()),
    path('create',StatusCreateAPIView.as_view()),
    # path('', StatusListSearchAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    path('<int:id>',StatusDetailAPIView.as_view()),
    path('<int:id>/update/',StatusUpdateAPIView.as_view()),
    path('<int:id>/delete/',StatusDeleteAPIView.as_view()),
]
#  api/status/create