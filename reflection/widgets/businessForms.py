'''
Created on 9 Feb 2017

@author: Lennon
'''

from django import forms

class NewResearchForm(forms.Form):
    question = forms.Textarea(label = 'Hypothesis or Question *')
    question_alias = forms.CharField(label = 'Proposed alias for question', max_length=50)
    question_detail = forms.Textarea(label = 'Detail about your question *')
    topic_area = forms.CharField(label = 'Propose a topic area *', max_length=200)
    topic_detail = forms.Textarea(label = 'Topic detail *')
    contact_email = forms.EmailInput(label = 'Contact Email')
    