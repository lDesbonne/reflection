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

def home(request):
    # Initialize global data about running projects
    approvalProcessing.initGlobalData()
    return render(request,'reflection/home.html')

def contribute(request):
    return render(request,'reflection/contribute.html')

def newResearchConcept(request):
    conceptForm = bForms.NewResearchForm()
    return render(request, 'reflection/concepts.html', {'researchForm':conceptForm})

def proposal(request):
    # TODO retrive form data and persist to the database
    formData = bForms.NewResearchForm(request.POST)
    
    persisted = utilities.storeProposal()
    return persisted
    
