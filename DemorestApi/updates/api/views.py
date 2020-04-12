from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

from updates.views import HttpResponseMixin
from updates.forms import UpdateModelForm
from .mixins import CSRFExemptMixin
from .utils import isjson_check
import json

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Detail Retrive , Update, Delete --> Object
    '''
    is_json = True
    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        # print("HEY !!!!!")
        # print(request.GET['id'])
        # id = request.GET['id']
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status =404)
        json_data = obj.serialize()
        # return HttpResponse(json_date, content_type='application/json')
        return self.render_to_response(json_data)
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"message":"Not allowed, please use the /api/update/ endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):

        if not isjson_check(request.body):
            error_data = json.dumps({"message": "Invalid data set, please send using JSON."})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        # print(dir(request))
        print(request.body)

        new_data = json.loads(request.body)
        passed_data = json.loads(request.body)
        data = json.loads(obj.serialize())

        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        print(new_data['content'])
        # print(request.data)
        json_data = json.dumps({"mesaage":"Somthing"})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=403)
        deleted_ = obj.delete()
        print(deleted_)
        if deleted_ == 1:
            json_data = json.dumps({"mesaage":"Successfully deleted id="+str(id)})
            return self.render_to_response(json_data, status=403)

        error_data = json.dumps({"message": "Could not delete item. Please try again later."})
        return self.render_to_response(error_data, status=400)

# AUTH / Permissions -- DJANGO REST FEAMEWORK -- Dont Use Tastypie
class UpdateModelListAPIView(HttpResponseMixin ,CSRFExemptMixin, View):
    '''
        List View
        Create View
    '''

    is_json = True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs
    def get_object(self, id=None):
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"id": "Object not found."})
                return self.render_to_response(error_data, status=400)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        if not isjson_check(request.body):
            error_data = json.dumps({"message":"Invalid data set, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        data = json.loads(request.body)
        print(request.POST)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({"message": "Not Allowed"})
        # form = UpdateModelForm
        return self.render_to_response(data, status=400)

    def put(self, request, *args, **kwargs):

        if not isjson_check(request.body):
            error_data = json.dumps({"message": "Invalid data set, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({"id": "This is a required fieldto update an item."})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_data, status=404)
        # print(dir(request))
        print(request.body)

        new_data = json.loads(request.body)

        data = json.loads(obj.serialize())

        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        print(new_data['content'])
        # print(request.data)
        json_data = json.dumps({"mesaage":"Somthing"})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        if not isjson_check(request.body):
            error_data = json.dumps({"message": "Invalid data set, please send using JSON."})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({"id": "This is a required fieldto update an item."})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        # obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_data, status=404)

        deleted_ = obj.delete()
        print("deleted_=>",deleted_[1]['updates.Update'])
        if deleted_[1]['updates.Update']:
            json_data = json.dumps({"mesaage":"Successfully deleted id="+str(passed_id)})
            return self.render_to_response(json_data, status=403)

        error_data = json.dumps({"message": "Could not delete item. Please try again later."})
        return self.render_to_response(error_data, status=400)


    # def delete(self, request, *args, **kwargs):
    #     is_json = True
    #     data = json.dumps({"message": "You Cannot delete a List"})
    #     return self.render_to_response(data, status=403)
