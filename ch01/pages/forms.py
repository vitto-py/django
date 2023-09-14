from django import forms


class createNew(forms.Form):
    name = forms.CharField(label="Name", max_length=20)
    check = forms.BooleanField(required=False)
