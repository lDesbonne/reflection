'''
Holds database tables linked to research proposals
Created on 29 Jan 2017

@author: Lennon
'''

from django.db import models
from django.db.models.deletion import CASCADE

# Topic area suggestions will be placed here for approval
class TopicAreas(models.Model):
    topic_area = models.CharField(max_length = 200, primary_key = True)
    detail = models.TextField()
    status = models.BooleanField("approval_status", default = False)

# Research proposals will be placed here for approval
class ResearchProposals(models.Model):
    proposal = models.CharField(max_length = 200, primary_key=True)
    detail = models.TextField()
    topic = models.ForeignKey(TopicAreas, on_delete=models.CASCADE)
    status = models.BooleanField("approval_status", default = False)
    
