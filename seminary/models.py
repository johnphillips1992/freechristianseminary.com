from django.db import models

from django.contrib.auth.models import User

from djangocms_text_ckeditor.fields import HTMLField

from cms.models import CMSPlugin

class Degree(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	certificate = models.FileField(upload_to='certificate', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	degree = models.ForeignKey(Degree, related_name='courses')
	certificate = models.FileField(upload_to='certificate', blank=True, null=True)
	def __unicode__(self):
		return '%s %s' % (self.degree.name, self.name)

class Section(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	course = models.ForeignKey(Course, related_name='sections')
	content = HTMLField(blank=True, null=True)
	video_url = models.CharField(max_length=512, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return '%s %s %s' % (self.course.degree.name, self.course.name,  self.name)

class Question(models.Model):
	course = models.ForeignKey(Course, related_name='questions')
	question = models.TextField(blank=False, null=False)
	answer_a = models.TextField(blank=True, null=True)
	answer_b = models.TextField(blank=True, null=True)
	answer_c = models.TextField(blank=True, null=True)
	answer_d = models.TextField(blank=True, null=True)
	correct_answer = models.CharField(max_length=1, blank=True, null=True,
				choices=(
					('A', 'A'),
					('B', 'B'),
					('C', 'C'),
					('D', 'D')))

class Score(models.Model):
	user = models.ForeignKey(User, related_name='+')
	course = models.ForeignKey(Course, related_name='scores')
	date = models.DateTimeField(auto_now_add=True)
	score = models.PositiveIntegerField(blank=False, null=False)
	def __unicode__(self):
		return '%s %s %s' % (self.user.username, self.course.name, self.date)

class Comment(models.Model):
	user = models.ForeignKey(User, related_name='comments')
	section = models.ForeignKey(Section, related_name='comments')
	content = models.TextField(blank=True, null=True)
	is_approved = models.BooleanField()
	def __unicode__(self):
		return '%s: %s' % (self.user.username, self.content)

class SectionPlugin(CMSPlugin):
	sections = models.PositiveIntegerField(blank=True, null=True)

