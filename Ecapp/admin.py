from django.contrib import admin

# Register your models here.
from .models import category,product

class categoryAdmin(admin.ModelAdmin):
    list_display=['slug','name']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryAdmin)


class productAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','avilable','created','updated']
    list_editable = ['price','stock','avilable']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productAdmin)
