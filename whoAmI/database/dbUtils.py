'''
Created on 28 Oct 2016

Contains helper functions associated with database persistence

@author: Lennon
'''
from . import sqliteData
from whoAmI.models import Word
import sqlite3
from django.db import connection

#databaseName = 'db.sqlite3'

def saveDocument(wordList, classified):
    for word in wordList:
        if sqliteData.queryWord(word):
            sqliteData.updateWord(word, classified)
        else:
            sqliteData.newWord(word, classified)
    
    # Update document number for whoAmI
    if sqliteData.queryDoc("whoAmI"):
        sqliteData.updateDoc("whoAmI")
    else:
        sqliteData.newDoc("whoAmI")
    
def synonymDetection():
    # TODO create method for synonym detection
    return None 

def execQuery(queryString):
    #conn = sqlite3.connect(databaseName)
    cursor = connection.cursor()
    cursor.execute(queryString)
    return cursor.fetchall()
     
