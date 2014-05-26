from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from seminary import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(),
	name='home'),
)

