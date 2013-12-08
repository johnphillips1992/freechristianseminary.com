from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404

from seminary import models 

class DegreeListView(ListView):
	model = models.Degree

class CourseListView(ListView):
	model = models.Course

	def get_degree(self):
		pk = self.kwargs.get('pk', None)
		
		return get_object_or_404(models.Degree, pk=pk)

	def get_context_data(self, **context):
		context = super(CourseListView, self).get_context_data(**context)

		context['degree'] = self.get_degree()
		return context

	def get_queryset(self):
		qs = super(CourseListView, self).get_queryset()

		degree = self.get_degree()

		return qs.filter(degree=degree)	

class SectionListView(ListView):
	model = models.Section

	def get_course(self):
		pk = self.kwargs.get('course_pk', None)
		return get_object_or_404(models.Course, pk=pk)

	def get_degree(self):
		pk = self.kwargs.get('degree_pk', None)
		return get_object_or_404(models.Degree, pk=pk)

	def get_context_data(self, **context):
		context = super(SectionListView, self).get_context_data(**context)

		context['course'] = self.get_course()
		context['degree'] = self.get_degree()
		return context

	def get_queryset(self):
		qs = super(SectionListView, self).get_queryset()

		course = self.get_course()

		return qs.filter(course=course)

class SectionDetailView(DetailView):
	model = models.Section

	def get_object(self):
		pk = self.kwargs.get('section_pk', None)
		return get_object_or_404(models.Section, pk=pk)

