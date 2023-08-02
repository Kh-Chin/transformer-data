from django import forms


class CustomForm(forms.Form):
    job_title = forms.CharField(max_length=100)
    company_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    keywords = forms.CharField(max_length=200)