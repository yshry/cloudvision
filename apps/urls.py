from django.conf.urls import url

from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^result/(?P<detection_type>([A-Z]+_*)+)/$', views.result, name='result'),
]
