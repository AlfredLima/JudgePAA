from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^view/', views.post_list),
    url(r'^submissions/', views.submissions_table),
    url(r'ajax/submissions/', views.get_submissions, name='get_submissions'),
    url(r'submit', views.post_new),
    url(r'^', RedirectView.as_view(url='/submit', permanent=False))
]
