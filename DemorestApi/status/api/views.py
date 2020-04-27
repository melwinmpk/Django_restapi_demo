from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from  rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
import json
# from django.views.generic


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusDetailAPIView(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' # if the lookup_field is not defined then pk will be expected by default

    def get_object(self, *args, **kwargs): # slug method for handeling the
        kwargs = self.kwargs
        kw_id  = kwargs.get('id')
        return Status.objects.get(id=kw_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly] # IsAuthenticated
    authentication_classes      = [SessionAuthentication]
    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    passed_id                   = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




'''
    StatusDetailAPIView which is commented is equivalent to the StatusDetailAPIView which is not
    uncommented one used mixins individually but the generic api view uses combined 
    '''


'''
    Currently not in use the below code
'''
class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field = 'id'  # if the lookup_field is not defined then pk will be expected by default

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field = 'id'  # if the lookup_field is not defined then pk will be expected by default
