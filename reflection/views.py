'''
Created on 19 Oct 2016

@author: Lennon
'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from . import utilities
from reflection.proposal import approvalProcessing
from reflection.widgets import businessForms as bForms
import json

def home(request):
    # Initialize global data about running projects
    if (not approvalProcessing.initialized):
        approvalProcessing.initGlobalData()
    return render(request,'reflection/home.html')

#TODO perhaps remove from here
def contribute(request):
    return render(request,'reflection/contribute.html')

def newResearchConcept(request):
    conceptForm = bForms.NewResearchForm()
    return render(request, 'reflection/concepts.html', {'researchForm':conceptForm,
                                                        'liveTopics':approvalProcessing.liveTopicAreas, 
                                                        'existingQuestions':approvalProcessing.liveStudies})

def submitProposal(request):
    #The presence of & may be causing parsing issues from the client
#     request_decode = request.body.decode('utf-8')
    #formData = bForms.NewResearchForm(request.POST)
    
    if (utilities.storeProposal(request.POST)):
        return render(request, 'plugins/messageBox.html', {'message':"Successfully submitted proposal"})
    else:
        #TODO improve the failure message
        return render(request, 'plugins/messageBox.html', {'message':"Failed to submit proposal"})
    
