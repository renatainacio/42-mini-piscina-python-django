from django import forms

class MyForm(forms.Form):
    input = forms.CharField(label="Input here")