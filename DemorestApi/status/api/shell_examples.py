# from django.utils.six import BytesIO
import io
from rest_framework.rendererd import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

'''
Serialize a single object
'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parser(stream)
print(data)

'''
Serialize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parser(stream2)
print(data2)

'''
Create obj
'''
data = {'user':1}
serializer = StatusSerializer(data=data)
if serializer.is_valid():
    serializer.save()
'''
Update Obj
'''
obj = Status.objects.first()
data = {'content': 'some new content',"user":1}
update_serializer = StatusSerializer(obj,data=data)
if update_serializer.is_valid():
    update_serializer.save()
else:
    print(update_serializer.errors)

'''
Delete Obj
'''
data = {'user':1,'content':'please Delete Me'}
create_obj = StatusSerializer(data=data)
if create_obj.is_valid():
    create_obj.save()
print(create_obj)


data = {'id':4}
obj = Status.objects.get(id=4)
update_serializer = StatusSerializer(obj)
update_serializer.data

obj.delete()
