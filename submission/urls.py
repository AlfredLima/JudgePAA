from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view/', views.post_list),
	url(r'', views.post_new),
]