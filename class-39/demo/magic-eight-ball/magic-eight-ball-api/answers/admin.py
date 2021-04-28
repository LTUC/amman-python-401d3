from django.contrib import admin
from .models import Answer, AnsweredQuestion

# Register your models here.
admin.site.register((Answer, AnsweredQuestion))
