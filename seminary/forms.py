from django import forms

from seminary import models

class CommentForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = ['content']

