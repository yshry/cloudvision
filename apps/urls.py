from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name = 'index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^result/(?P<detection_type>([A-Z]+_*)+)/$', views.result, name='result'),
    url(r'^login/', views.my_login, name='login'),
    url(r'^logout/', views.my_logout, name='logout'),
]
