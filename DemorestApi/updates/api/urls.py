from django.contrib import admin
from django.urls import path, include, re_path

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView
)

urlpatterns = [
    path('',UpdateModelListAPIView.as_view()),
    path('<int:id>',UpdateModelDetailAPIView.as_view())
    # ^(?P<id>\d+)/$
    # path('json/example',json_example_view, name=''),
    # path('json/classexample1',JsonCBV.as_view(), name=''),
    # path('json/classexample2',JsonCBV2.as_view(), name=''),
    # path('json/serialized/list',SerizlizedListView.as_view(), name=''),
    # path('json/serialized/detail',SerizlizedDetailView.as_view(), name='')
]
