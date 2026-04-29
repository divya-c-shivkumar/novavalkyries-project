from django.contrib import admin
from .models import Subject, Module, CO, COPOMapping

admin.site.register(Subject)
admin.site.register(Module)
admin.site.register(CO)
admin.site.register(COPOMapping)

