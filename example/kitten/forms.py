from django import forms
from .models import Kitten
from s3direct.widgets import S3DirectFileWidget, S3DirectURLWidget


class KittenForm(forms.ModelForm):
	class Meta:
		model = Kitten
		widgets = {
			'file': S3DirectFileWidget(upload_to='foo'),
		}