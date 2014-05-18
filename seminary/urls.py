from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from seminary import views

urlpatterns = patterns('',
    url(r'^game/$', TemplateView.as_view(template_name="seminary/game.html")),
    url(r'^$', views.DegreeListView.as_view(),
	name='degree-list'),
    url(r'^degrees/(?P<pk>\d+)/courses/$', views.CourseListView.as_view(),
	name='course-list'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/sections/$',
	views.SectionListView.as_view(), name='section-list'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/sections/(?P<section_pk>\d+)/$',
	views.SectionDetailView.as_view(), name='section-detail'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/test/$',
	login_required(
		views.TestView.as_view()), name='test'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/scores/$',
	login_required(
		views.ScoreListView.as_view()), name='score-list'),
    url(r'^degrees/(?P<degree_pk>\d+)/courses/(?P<course_pk>\d+)/score/(?P<score>\d+)/$',
	views.ScoreView.as_view(), name='score'),
    url(r'^accounts/create/$',
	views.UserCreationView.as_view(), name='account-creation'),
)

