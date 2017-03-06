'''
Created on 9 Feb 2017

@author: Lennon
'''

from django import forms

class NewResearchForm(forms.Form):
    question = forms.CharField(label = 'Hypothesis or Question *', widget = forms.Textarea)
    question_alias = forms.CharField(label = 'Proposed alias for question', max_length=50)
    question_detail = forms.CharField(label = 'Detail about your question *', widget = forms.Textarea)
    topic_area = forms.CharField(label = 'Propose a topic area *', max_length=200)
    topic_alias = forms.CharField(label = 'Alias for topic', max_length = 20)
    topic_detail = forms.CharField(label = 'Topic detail *', widget = forms.Textarea)
    contact_email = forms.CharField(label = 'Contact Email', widget = forms.EmailInput)
    