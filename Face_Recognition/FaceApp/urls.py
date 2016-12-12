from django.contrib import admin
app_name = 'FaceApp'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.get_chart, name='get_chart'),
]
