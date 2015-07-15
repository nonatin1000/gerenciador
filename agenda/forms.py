from django import forms
from django.forms import ModelForm
from models import ItemAgenda

class FormItemAgenda(forms.ModelForm):
	class Meta:
		model = ItemAgenda
		fields = ['titulo', 'data', 'hora', 'descricao', 'participantes']