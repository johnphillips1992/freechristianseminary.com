from django.contrib import admin
from seminary import models 



class QuestionInline(admin.StackedInline):
        model = models.Question
        extra = 3

class CourseInline(admin.StackedInline):
	model = models.Course
	extra = 2

class DegreeAdmin(admin.ModelAdmin):
	inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
	inlines = [QuestionInline]

admin.site.register(models.Degree, DegreeAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Section)
admin.site.register(models.Question)
admin.site.register(models.Score)
