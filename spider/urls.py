from django.conf.urls import url

from . import views

app_name = 'spider'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^status$', views.Status, name='status'),
    url(r'^run$', views.Run, name='run'),
]