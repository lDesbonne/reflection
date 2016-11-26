'''
Created on 19 Oct 2016

@author: Lennon
'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from . import utilities

def home(request):
    return render(request,'reflection/home.html')

def contribute(request):
    return render(request,'reflection/contribute.html')

def proposal(request, prop):
    persisted = utilities.storeProposal(prop)
    return persisted
    
