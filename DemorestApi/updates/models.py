from django.core.serializers import serialize
from django.conf import settings
from django.db import models
import json
# Create your models here.
def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # First Method
    # def serialize(self):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))

    # Second Method
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     print("hey12")
    #     for obj in qs:
    #         stuct = json.loads(obj.serialize())
    #         final_array.append(stuct)
    #     return json.dumps(final_array)
    def serialize(self):
        list_values = list(self.values("id", "user", "content", "image"))
        return json.dumps(list_values)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()
    def __str__(self):
        return self.content or ""

    # First Method
    # def serialize(self):
    #     print("hey!!!")
    #     json_data = serialize("json", [self], fields=('user', 'content', 'image'))
    #     stuct = json.loads(json_data)
    #     data = json.dumps(stuct[0]['fields'])
    #     return data

    def serialize(self):
        try:
            image = self.imge.url
        except:
            image = ""
        data = {
            "id"     : self.id,
            "content": self.content,
            "user"   : self.user.id,
            "image"  : image
        }

        data = json.dumps(data)
        return data