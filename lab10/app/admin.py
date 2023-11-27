from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Note, Topic

# Register your models here.
admin.site.register(Note)

class TopicAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'public')
    list_editable = ('public',)

admin.site.register(Topic, TopicAdmin)
