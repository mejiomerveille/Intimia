from django import forms
from .models import Code

class CodeForm(forms.Form):
    input1 = forms.CharField(label="",required=True ,max_length=1,min_length=1)
    input2= forms.CharField(label="",required=True ,max_length=1,min_length=1)
    input3 = forms.CharField(label="",required=True,max_length=1,min_length=1)
    input4 = forms.CharField(label="",required=True,max_length=1,min_length=1)
    input5 = forms.CharField(label="",required=True,max_length=1,min_length=1)
    # input6 = forms.CharField(label="",required=True,max_length=1,min_length=1)