from django.contrib import admin
from.models import Contact
# from.models import Index

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display=['id','name','email','phone','message']

# @admin.register(Index) 
# class Index(admin.ModelAdmin) :
#     list_display=['id','name','email','phone','message']
