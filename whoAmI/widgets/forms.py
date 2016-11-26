'''
Created on 22 Oct 2016

Contains form objects for use in the Who Am I study

@author: Lennon
'''
from django import forms

class SelfDescribeForm(forms.Form):
    word1 = forms.CharField(max_length=50)
    word2 = forms.CharField(max_length=50)
    word3 = forms.CharField(max_length=50)
    word4 = forms.CharField(max_length=50)
    word5 = forms.CharField(max_length=50)