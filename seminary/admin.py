from django.contrib import admin
from seminary import models 



class QuestionInline(admin.StackedInline):
        model = models.Question
        extra = 3

class CourseInline(admin.StackedInline):
	model = models.Course
	extra = 2

class DegreeAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines = [QuestionInline]

class SectionAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']

admin.site.register(models.Degree, DegreeAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Score)
