from django.contrib import admin
from.models import *

# Register your models here.
admin.site.Register(user)
admin.site.Register(doctor)
admin.site.Register(patient)