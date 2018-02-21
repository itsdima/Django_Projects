from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index), 
	url(r'^courses$', views.index), 
	url(r'^courses/destroy/(?P<number>\d+)$', views.destroy),
	url(r'^courses/destroy/(?P<number>\d+)/process$', views.process), 
	url(r'^add$', views.add)
]