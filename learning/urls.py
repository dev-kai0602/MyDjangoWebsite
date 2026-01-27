""" 定义 learning 的 URL 模式 """
from django.urls import path

from . import views

app_name = 'learning'
urlpattern = [
    path('', views.index, name='index'),
]
