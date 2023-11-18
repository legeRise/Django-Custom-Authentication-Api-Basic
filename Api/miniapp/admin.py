from django.contrib import admin
from .models import Information
# Register your models here.


@admin.register(Information)
class info(admin.ModelAdmin):
    list_display  = ['username','password','confirm']             # the name 'list_display' is a must