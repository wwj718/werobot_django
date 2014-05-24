#coding = utf-8
import sys , os
from datetime import *
import django

sys.path.append('/home/wwj/mylab/waibao/yaxiuji/werobot_django/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

#only in django1.4 can use setup_environ , 1.6 will cause error
from django.core.management import setup_environ

from mysite import settings

from myblog.models import Blog

setup_environ(settings)

blogs = Blog.objects.all()[0].title
print blogs

