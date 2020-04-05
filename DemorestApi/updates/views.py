from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from .models import Update
import json


def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
# Create your views here.

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)
    def get_data(self, context):
        return context

class JsonCBV2(JsonResponseMixin,View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)

class SerizlizedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # data = serialize("json", qs, fields=('user', 'content'))
        # data = serialize("json", [obj,])
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

class SerizlizedListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Update.objects.all()
        # data = serialize("json", qs, fields=('user', 'content'))
        # data = serialize("json", qs)
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')