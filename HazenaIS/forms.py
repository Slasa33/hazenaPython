from django import forms
from HazenaIS.models import Hrac, Klub, Zapasy

class ZapasSearchForm(forms.Form):
    searched_name = forms.CharField(max_length=50, label='Klub')

class HracForm(forms.ModelForm):
    class Meta:
        model = Hrac
        exclude = []

class KlubForm(forms.ModelForm):
    class Meta:
        model = Klub
        exclude = []

class ZapasyForm(forms.ModelForm):
    class Meta:
        model = Zapasy
        exclude = []