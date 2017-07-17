from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from genPerGen.calculate import naiveAlgo
from genPerGen.widgets import forms
from genPerGen.database import dbUtils, sqliteData
from genPerGen.calculate.analytics import GenPerGenStats
from reflection.models import ResearchProposals as research
from genPerGen import models
import json

def studyActive():
    return research.objects.filter(id = models.STUDY_ID, status = 1).exists()

def predictGender(request):
    if not studyActive():
        return None
    
    # Retrieve the prediction and other info
    wordList = []
    formData = forms.SelfDescribeForm(request.POST)
    if formData.is_valid():
        wordList.append(formData.cleaned_data['word1'])
        wordList.append(formData.cleaned_data['word2'])
        wordList.append(formData.cleaned_data['word3'])
        wordList.append(formData.cleaned_data['word4'])
        wordList.append(formData.cleaned_data['word5'])
    else:
        return render(request, 'genPerGen/404.html')   
    
    
    classified, notFound = naiveAlgo.classifyGender(wordList)
    
    context = {
               'classified':classified,
               'word_notFound':notFound,
               'wordList':wordList,
               }
    
    return render(request, 'genPerGen/results.html', context)

def home(request):
    return render(request, 'reflection/home.html')

def dataIn(request):
    if not studyActive():
        return None
    
    descriptionForm = forms.SelfDescribeForm()
    return render(request, 'genPerGen/predInput.html', {'describe':descriptionForm})

@csrf_protect
def breakdown(request):
    if not studyActive():
        return None
    
    data_decode = request.body.decode('utf-8')
    data = json.loads(data_decode)
    wordsUsed = data['wordlist']
    notFound = data['exlist']
    
    #Constructs the original dataset
    def initialData(exlist,usedWords):
        words = []
        for word in usedWords:
            if word != "NotPresent":
                words.append(word)
        for w in exlist:
            words.append(w)
        return words
    
    # Evaluate whether the words can be submitted to the database
    numDoc = sqliteData.numberDocs()
    if(numDoc < 1000):
        if(data['accurate'] != "noData"):
            if(data['gender'] == "Female"):
                dbUtils.saveDocument(initialData(notFound, wordsUsed), 0, data['accurate'])
            elif(data['gender'] == "Male"):
                dbUtils.saveDocument(initialData(notFound, wordsUsed), 1, data['accurate'])
    
    # Retrieve statistics info for the words submitted
    gpgStats = GenPerGenStats(wordsUsed)
    
    # Retrieve top 10 words by gender
            
    context = {
             'notFound':notFound,
             'accurate':data['accurate'],
             'entries':numDoc,
             'accuracy':gpgStats.successRate,
             'topF':gpgStats.topFWords,
             'topM':gpgStats.topMWords,
             }
    
    return render(request, 'genPerGen/breakdown.html', context)
