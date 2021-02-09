from django.contrib import admin
from fakerjobsApp.models import Hydjobs,Banglorejobs,Chennaijobs,Punejobs


class HydAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BanglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']



# Register your models here.
admin.site.register(Hydjobs,HydAdmin)
admin.site.register(Banglorejobs,BanglorejobsAdmin)
admin.site.register(Chennaijobs,ChennaijobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)
