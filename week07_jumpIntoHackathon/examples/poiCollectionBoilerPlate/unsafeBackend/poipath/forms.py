from django import forms
from .models import poi, sns, extlnk, tag


class poiForm(forms.ModelForm):
    class Meta:
        model = poi
        fields = ['name', 'lat', 'lng']


class snsForm(forms.ModelForm):
    class Meta:
        model = sns
        fields = ['name', 'api_root']


class extlnkForm(forms.ModelForm):
    class Meta:
        model = extlnk
        fields = ['url', 'relsns', 'relpoi']


class tagForm(forms.ModelForm):
    class Meta:
        model = tag
        fields = ['name', 'proposer', 'relpoi']


