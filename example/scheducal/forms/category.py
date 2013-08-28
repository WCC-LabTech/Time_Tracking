from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    is_project = forms.BooleanField(required=False)
