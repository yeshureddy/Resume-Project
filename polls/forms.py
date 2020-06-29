from django import forms
from . models import extrafield


class Extrafielfform(forms.ModelForm):
	class Meta:
		model = extrafield
		fields = ['field_name','explanation']

			
	