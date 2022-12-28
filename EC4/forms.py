from django import forms

class FormArticulo(forms.Form):
    name = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=100)
    state = forms.CharField(max_length=20)