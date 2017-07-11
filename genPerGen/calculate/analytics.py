'''
Created on 28 Oct 2016

Contains functions that provide statistical information 
regarding the "Who Am I?" project.

@author: Lennon
'''

from genPerGen.database import dbUtils, sqliteData
from genPerGen import models

#Query for top 10 words used by woman
topFQuery = "SELECT * FROM genPerGen_word WHERE cFem != 0 ORDER BY cFem DESC LIMIT 10"
#Query for top 10 words used by men
topMQuery = "SELECT * FROM genPerGen_word WHERE cMale != 0 ORDER BY cMale DESC LIMIT 10"

#TODO finish implementing accuracy updates.
class GenPerGenStats(object):
    
    def __init__(self, wordlist = []):
        self.topMWords = self.__getWordlist(topMQuery)
        self.topFWords = self.__getWordlist(topFQuery)
        self.successRate = self.calcSuccess()
        #self.confidence = 0
        self.words = self.getUsedWords(wordlist)
        
    # TODO Calculates the confidence of the current prediction
    def __calcConfidence(self):
        #Need the probability values from the naiveAlgo...
        pass
    
    def __getWordlist(self,query):
        # Modify the query with the study in question
        
        results = dbUtils.execQuery(query)
        words = []
        for result in results:
            words.append(result[1])
        
        return words
            
    
    def calcSuccess(self):      
        # Query the who am i research study
        if sqliteData.queryDoc(models.ASSOCIATED_STUDY):
            researchQ = models.Data.objects.get(study_title = models.ASSOCIATED_STUDY)
            return round(researchQ.successes/(researchQ.fails + researchQ.successes)*100,1)
        else:
            return 0
            
            
    
    def getUsedWords(self,wrds):
        wordsUsed = []
        for word in wrds:
            #wordsUsed.append(sqliteData.getWord(word))
            wordsUsed.append(word)
        
        return wordsUsed
    