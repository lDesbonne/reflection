'''
Created on 2 Oct 2016

@author: Lennon

Module contains methods compatible with sqlite3
'''

from genPerGen import models
from django.core.exceptions import ObjectDoesNotExist

#Retrieves word from the naivePredictor_word table
def queryWord(descWord,study_key = models.STUDY_TITLE):
    try:
        dbWord = models.Word.objects.get(word=descWord, study = study_key)
        if dbWord != None:
            return True
            
    except ObjectDoesNotExist:
        print("\""+descWord+"\" not found in the database, will exclude from current prediction")
        return False

def queryDoc(docName = models.STUDY_TITLE):
    try:
        doc = models.ResearchQuery.objects.get(study_title = docName)
        if doc != None:
            return True
    except ObjectDoesNotExist:
        print("\""+docName+"\" study does not exist")
        return False
    
#Adds a new word to the naivePredictor_word table
def newWord(descWord, classified, study_key = models.STUDY_TITLE):
    if classified is 1:
        dbWord = models.Word(word = descWord,cMale=1, study=study_key)
        dbWord.save()
    else:
        dbWord = models.Word(word = descWord, cFem=1, study=study_key)
        dbWord.save()
    
    print("\""+descWord+"\" added to the database")

#Retrieves the number of documents for which we have data
def numberDocs(docuname = models.STUDY_TITLE):
    try:
        study = models.ResearchQuery.objects.get(study_title = docuname)
        return study.num_docs
    except ObjectDoesNotExist:
        # TODO improve the error handling
        return 0
    
def docSuccessRate(docuname = models.STUDY_TITLE):
    try:
        study = models.ResearchQuery.objects.get(study_title = docuname)
        return study.successRate()
    except ObjectDoesNotExist:
        return 0

def newDoc(docuname = models.STUDY_TITLE, success = False):
    # Check to see if the query exists and has been approved
    if success:
        doc = models.ResearchQuery(study_title = docuname, num_docs = 1, successes = 1, fails = 0)
    else:
        doc = models.ResearchQuery(study_title = docuname, num_docs = 1, successes = 0, fails = 1)
    doc.save()

def updateDoc(success, docuname = models.STUDY_TITLE):
    doc = models.ResearchQuery.objects.get(study_title = docuname)
    doc.num_docs += 1
    if success:
        doc.successes += 1
    else:
        doc.fails += 1
    doc.save()

def updateWord(descWord, classified, study_key = models.STUDY_TITLE):
    dbWord = models.Word.objects.get(word = descWord, study = study_key)
    if classified is 1:
        #Update the male count
        dbWord.cMale += 1
    else:
        dbWord.cFem += 1
    
    dbWord.save()

def getAllWords():
    return models.Word.objects.all()

def getWord(wrd, study_key = models.STUDY_TITLE):
    return models.Word.objects.get(word = wrd, study=study_key)
    