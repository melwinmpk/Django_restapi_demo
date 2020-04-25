from rest_framework import generics, mixins
from rest_framework.views import APIView
from  rest_framework.response import Response
from status.models import Status
from .serializers import StatusSerializer
from django.shortcuts import get_object_or_404
# from django.views.generic



class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    # queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request   = self.request
        passed_id = request.GET.get('id', None)
        queryset   = self.get_queryset()
        obj        = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


'''
    StatusDetailAPIView which is commented is equivalent to the StatusDetailAPIView which is not
    uncommented one used mixins individually but the generic api view uses combined 
    '''

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'  # if the lookup_field is not defined then pk will be expected by default

class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' # if the lookup_field is not defined then pk will be expected by default

    # def get_object(self, *args, **kwargs): # slug method for handeling the
    #     kwargs = self.kwargs
    #     kw_id  = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
