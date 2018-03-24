from django import forms

class ChoisListForm(forms.Form):
    chos=forms.BooleanField(required=False, initial=False,)