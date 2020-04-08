from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
from updates.views import HttpResponseMixin
from .mixins import CSRFExemptMixin
import json

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Detail Retrive , Update, Delete --> Object
    '''
    is_json = True
    def get(self, request, id, *args, **kwargs):
        # print("HEY !!!!!")
        # print(request.GET['id'])
        # id = request.GET['id']
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        # return HttpResponse(json_date, content_type='application/json')
        return self.render_to_response(json_data)
    def post(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)


class UpdateModelListAPIView(HttpResponseMixin ,CSRFExemptMixin, View):
    '''
        List View
        Create View
    '''

    is_json = True
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):

        data = json.dumps({"message": "Unknown data"})
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        is_json = True
        data = json.dumps({"message": "You Cannot delete a List"})
        return self.render_to_response(data, status=403)
