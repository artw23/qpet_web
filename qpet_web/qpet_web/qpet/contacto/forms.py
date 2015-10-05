from django import forms

class ContactoForm(forms.Form):
    nombre_completo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mensaje = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    