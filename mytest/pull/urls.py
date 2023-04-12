from django.urls import path

from . import views
urlpatterns = [
	path('', views.hello_world, name='index'),#这个name是映射到views.index

]