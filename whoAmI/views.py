from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from whoAmI.calculate import naiveAlgo
from whoAmI.widgets import forms
from whoAmI.database import dbUtils, sqliteData
from whoAmI.calculate.analytics import WhoAmIStats
import json

def predictGender(request):
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
        return render(request, 'whoAmI/404.html')   
    
    
    classified, notFound = naiveAlgo.classifyGender(wordList)
    
    context = {
               'classified':classified,
               'word_notFound':notFound,
               'wordList':wordList,
               }
    
    return render(request, 'whoAmI/results.html', context)

def home(request):
    return render(request, 'reflection/home.html')

def dataIn(request):
    descriptionForm = forms.SelfDescribeForm()
    return render(request, 'whoAmI/predInput.html', {'describe':descriptionForm})

@csrf_protect
def breakdown(request):
    data_decode = request.body.decode('utf-8')
    data = json.loads(data_decode)
    wordsUsed = data['wordlist']
    notFound = data['exlist']
    nf = [] # Words not found in the database
    
    # Generate list of words not in the database
    for i in range(len(notFound)):
        if (notFound[i] == "NotPresent"):
            nf.append(wordsUsed[i])
    
    # Evaluate whether the words can be submitted to the database
    numDoc = sqliteData.numberDocs("whoAmI")
    if(numDoc < 1000):
        if(data['accurate'] != "noData"):
            if(data['gender'] == "Female"):
                dbUtils.saveDocument(wordsUsed, 0)
            elif(data['gender'] == "Male"):
                dbUtils.saveDocument(wordsUsed, 1)
    
    # Retrieve statistics info for the words submitted
    whoStats = WhoAmIStats(wordsUsed)
    #TODO create an accuracy stat
    success = 1
    if not data['accurate']:
        succuess = 0
    accuracy = whoStats.calcSuccess(success)
    
    # Retrieve top 10 words by gender
            
    context = {
             'notFound':nf,
             'accurate':data['accurate'],
             'entries':numDoc,
             'accuracy':accuracy,
             'topF':whoStats.topFWords,
             'topM':whoStats.topMWords,
             }
    
    return render(request, 'whoAmI/breakdown.html', context)
