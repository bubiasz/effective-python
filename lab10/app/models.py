from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Note(TimeStampedModel):
    name = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Topic(TitleSlugDescriptionModel, TimeStampedModel, MPTTModel):
    name = models.CharField(max_length=100)
    public = models.BooleanField(default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
