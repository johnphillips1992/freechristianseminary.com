from cms.admin.placeholderadmin import FrontendEditableAdmin

from django.contrib import admin
from seminary import models 



class QuestionInline(admin.StackedInline):
        model = models.Question
        extra = 3

class CourseInline(admin.StackedInline):
	model = models.Course
	extra = 2

class SectionInline(admin.StackedInline):
	model = models.Section

class DegreeAdmin(FrontendEditableAdmin, admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines = [CourseInline]

class CourseAdmin(FrontendEditableAdmin, admin.ModelAdmin):
	list_display = ['__unicode__']
	inlines = [SectionInline, QuestionInline]

class SectionAdmin(FrontendEditableAdmin, admin.ModelAdmin):
	list_display = ['__unicode__']

class CommentAdmin(FrontendEditableAdmin, admin.ModelAdmin):
	list_display = ['__unicode__', 'user', 'section', 'is_approved']
	list_editable = ['is_approved']

admin.site.register(models.Degree, DegreeAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Section, SectionAdmin)
admin.site.register(models.Score)
admin.site.register(models.Comment, CommentAdmin)
