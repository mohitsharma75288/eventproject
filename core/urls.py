from django.conf.urls import url, include
from . import views
urlpatterns=[

    url('input/', views.input, name='input'),
    url('', views.show, name='show'),

    url('core/', views.core, name='core'),


    ]