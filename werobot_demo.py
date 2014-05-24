#coding=utf-8
# django settings.py
from django.conf import settings

settings.configure(
    DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
                        'USER': '',                      # Not used with sqlite3.
                        'PASSWORD': '',                  # Not used with sqlite3.
                        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
                    }
    },
        INSTALLED_APPS     = ("")
)
#==========

# werobot
# coding=utf-8
import werobot
robot = werobot.WeRoBot(token='myyunfan')  # 填写你的token


# use django orm
from myblog.models import Blog
first_title = Blog.objects.all()[0].title
print first_title


@robot.text
def echo(message):
        if message.content == 'a':
            return message.content
        if message.content == 'title':
            return first_title
# 只有之前的都没有匹配，handler最后被调用
@robot.handler
def hello(message):
        return 'Hello World!'
robot.run()
