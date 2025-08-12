from django import forms
from .models import Spare, Machine, Kit

class SpareForm(forms.ModelForm):
    class Meta:
        model = Spare
        fields = '__all__'