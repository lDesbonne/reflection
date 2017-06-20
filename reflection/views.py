'''
Created on 19 Oct 2016

@author: Lennon
'''
from django.shortcuts import render
from . import utilities
from reflection.proposal import approvalProcessing, AdministrationServices
from reflection.widgets import businessForms as bForms
from reflection.proposal import AdminUtilities
import json
from django.http import JsonResponse

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
    if (utilities.storeProposal(request.POST)):
        return render(request, 'plugins/messageBox.html', {'message':"Successfully submitted proposal"})
    else:
        #TODO improve the failure message
        return render(request, 'plugins/messageBox.html', {'message':"Failed to submit proposal"})
    
#Will allow someone to approve topics and questions
def adminApprovalDashboard(request):
    return render(request, 'reflection/currentprojectdata.html', {
                                                                  'liveData': liveAdministrationData(),
                                                                  'pendingData': pendingAdministrationData()})

def liveAdministrationData():
    live = AdministrationServices.approvalDataBuilder('Live')
    return AdminUtilities.approvalInfoToJsonString(live)

def pendingAdministrationData():
    pending = AdministrationServices.approvalDataBuilder('Pending')
    return AdminUtilities.approvalInfoToJsonString(pending)

