'''
Created on 28 Oct 2016

Contains helper functions associated with database persistence

@author: Lennon
'''
from . import sqliteData
from django.db import connection


def saveDocument(wordList, classified, researchQuery, success = False):
    for word in wordList:
        if sqliteData.queryWord(word):
            sqliteData.updateWord(word, classified, researchQuery)
        else:
            sqliteData.newWord(word, classified, researchQuery)
    
    if sqliteData.queryDoc(researchQuery):
        sqliteData.updateDoc(researchQuery, success)
    else:
        sqliteData.newDoc(researchQuery, success)
    
def synonymDetection():
    # TODO create method for synonym detection
    return None 

def execQuery(queryString):
    cursor = connection.cursor()
    cursor.execute(queryString)
    return cursor.fetchall()
     
