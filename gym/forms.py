from django import forms
from .models import Trainner

class TrainnerForm(forms.ModelForm):
    class Meta:
        model = Trainner
        fields = '__all__'
