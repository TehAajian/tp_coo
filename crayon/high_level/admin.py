from django.contrib import admin
from . import models

admin.site.register(models.IntegerField)
admin.site.register(models.CharField)
admin.site.register(models.ManyToManyField)
admin.site.register(models.ForeignKey)
