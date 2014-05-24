#coding:utf-8
from django.contrib import admin
#from django.contrib.markup.templatetags.markup import restructuredtext

from .models import Blog

#from django_admin_bootstrapped.widgets import GenericContentTypeSelect

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content')

admin.site.register(Blog, BlogAdmin)

