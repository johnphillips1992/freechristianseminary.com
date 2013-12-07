from django.db import models

from django.contrib.auth.models import User

class Degree(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	certificate = models.FileField(upload_to='certificate', blank=True, null=True)

class Course(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	degree = models.ForeignKey(Degree, related_name='courses')
	certificate = models.FileField(upload_to='certificate', blank=True, null=True)

class Section(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	course = models.ForeignKey(Course, related_name='sections')
	content = models.TextField(blank=True, null=True)

class Question(models.Model):
	course = models.ForeignKey(Course, related_name='questions')
	question = models.TextField(blank=False, null=False)
	answer_a = models.TextField(blank=True, null=True)
	answer_b = models.TextField(blank=True, null=True)
	answer_c = models.TextField(blank=True, null=True)
	answer_d = models.TextField(blank=True, null=True)
	correct_answer = models.CharField(max_length=1, blank=True, null=True)

class Score(models.Model):
	user = models.ForeignKey(User, related_name='+')
	course = models.ForeignKey(Course, related_name='scores')
	date = models.DateTimeField(auto_now_add=True)
	score = models.PositiveIntegerField(blank=False, null=False)
