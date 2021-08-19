from django.contrib import admin
from .models import Note, Section, Tag

admin.site.register(Note)
admin.site.register(Section)
admin.site.register(Tag)
