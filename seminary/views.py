from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic import  TemplateView
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

		return qs.filter(degree=degree).order_by('pk')	

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

		return qs.filter(course=course).order_by('pk')

class SectionDetailView(DetailView):
	model = models.Section

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if "comment" in request.POST:
				content = request.POST['content']
				comment = models.Comment.objects.create(content=content,
					user=request.user,
					section=self.get_object(),
					is_approved=False)
				comment.save()
				messages.success(request, 'Your comment has been submitted and is pending approval')
		return HttpResponseRedirect(reverse('section-detail', kwargs={'section_pk': self.get_object().pk, 
									      'degree_pk': self.get_object().course.degree.pk,
									      'course_pk': self.get_object().course.pk}))

	def get_context_data(self, **context):
		context = super(SectionDetailView, self).get_context_data(**context)
		return context

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

	def post(self, request, *args, **kwargs):
		print("%s" % request.POST)
		questions = self.get_queryset()
		score = 0
		if questions.all().count() > 0:
			for question in questions.all():
				question_pk = 'question_%s' % question.pk
				if question_pk in request.POST:
					answer = request.POST['question_%s' % question.pk]
					if answer == question.correct_answer:
						score = score + 100
			score = int(score/questions.all().count())
			course = self.get_course()
			models.Score.objects.create(user=request.user, course=course, score=score)
			return HttpResponseRedirect('/degrees/%s/courses/%s/score/%s/' % (course.degree.pk, course.pk, score))
		return HttpResponseRedirect('/degrees/%s/courses/%s/' % (course.degree.pk, course.pk))

	def get_queryset(self):
		qs = super(TestView, self).get_queryset()
		course = self.get_course()
		return qs.filter(course=course)

class ScoreView(TemplateView):
	template_name = 'seminary/score.html'

	def get_course(self):
		pk = self.kwargs.get('course_pk', None)
		return get_object_or_404(models.Course, pk=pk)

	def get_context_data(self, **context):
		context = super(ScoreView, self).get_context_data(**context)
		context['score'] = self.kwargs.get('score', None)
		context['course'] = self.get_course()
		return context

class ScoreListView(ListView):
	model = models.Score

	def get_course(self):
		pk = self.kwargs.get('course_pk', None)
		return get_object_or_404(models.Course, pk=pk)

	def get_context_data(self, **context):
		context = super(ScoreListView, self).get_context_data(**context)
		context['course'] = self.get_course()
		return context

	def get_queryset(self):
		qs = super(ScoreListView, self).get_queryset()
		return qs.filter(user=self.request.user, course=self.get_course())

class UserCreationView(FormView):
	form_class = UserCreationForm
	success_url = '/'
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
		

