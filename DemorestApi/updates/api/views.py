from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
import ast

class UpdateModelDetailAPIView(View):
    '''
    Detail Retrive , Update, Delete --> Object
    '''

    def get(self, request, id, *args, **kwargs):
        # print("HEY !!!!!")
        # print(request.GET['id'])
        # id = request.GET['id']
        obj = UpdateModel.objects.get(id=id)
        json_date = obj.serialize()
        return HttpResponse(json_date, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')


class UpdateModelListAPIView(View):
    '''
        List View
        Create View
    '''

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')

