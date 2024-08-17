from django import forms
from .models import TitanicPassenger

class UploadFileForm(forms.Form):
    file = forms.FileField()

class TitanicPassengerForm(forms.ModelForm):
    class Meta:
        model = TitanicPassenger
        fields = '__all__'