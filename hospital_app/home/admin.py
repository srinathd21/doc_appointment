from django.contrib import admin
from .models import *

# Register your models here.
class Doctorsadmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'avel_dates', 'in_out_time')

class patient(admin.ModelAdmin):
    list_display = ('name','contact','doctor')

admin.site.register(Catagory)
admin.site.register(Doctors,Doctorsadmin)
admin.site.register(UserProfile,patient)