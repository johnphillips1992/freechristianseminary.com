from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.views.generic.edit import FormView

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

class TestView(ListView):
	model = models.Question

	def get_course(self):
		pk = self.kwargs.get('course_pk', None)
		return get_object_or_404(models.Course, pk=pk)

	def get_context_data(self, **context):
		context = super(TestView, self).get_context_data(**context)
		context['course'] = self.get_course()
		return context

	def get(self, request, *args, **kwargs):
		return super(TestView, self).get(request, *args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		return super(TestView, self).post(request, *args, **kwargs)

	def get_queryset(self):
		qs = super(TestView, self).get_queryset()
		course = self.get_course()
		return qs.filter(course=course)

class UserCreationView(FormView):
	form_class = UserCreationForm
	success_url = '/degrees/'
	template_name = 'registration/create.html'

	def form_valid(self, form):
		if form.is_valid():
			username = form.clean_username()
			password = form.clean_password2()
			form.save()
			user = authenticate(username=username,
					    password=password)
			login(self.request, user)
		return super(UserCreationView, self).form_valid(form)
		

