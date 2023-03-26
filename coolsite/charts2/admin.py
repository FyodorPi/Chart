from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Chart)
admin.site.register(Kind)
admin.site.register(Consumer)
admin.site.register(Grade)