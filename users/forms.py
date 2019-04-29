from django import forms


class FormClient(forms.Form):
    FIO = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=200, required=False)
