from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from seminary import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="seminary/home.html")),
    url(r'^degrees/$', views.DegreeListView.as_view(),
	name='degree-list'),
    url(r'^degrees/(?P<pk>\d+)/courses/$', views.CourseListView.as_view(),
	name='course-list'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/sections/$',
	views.SectionListView.as_view(), name='section-list'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/sections/(?P<section_pk>\d+)/$',
	views.SectionDetailView.as_view(), name='section-detail'),
)

