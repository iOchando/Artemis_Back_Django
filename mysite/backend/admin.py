from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)