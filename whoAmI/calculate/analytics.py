'''
Created on 28 Oct 2016

Contains functions that provide statistical information 
regarding the "Who Am I?" project.

@author: Lennon
'''

from whoAmI.database import dbUtils, sqliteData
from whoAmI import models
from numpy import array
from string import Template

#Query for top 10 words used by woman
topFQuery = Template("SELECT * FROM whoAmI_word WHERE cFem != 0 AND study = $study ORDER BY cFem DESC LIMIT 10")
#Query for top 10 words used by men
topMQuery = Template("SELECT * FROM whoAmI_word WHERE cMale != 0 AND study = $study ORDER BY cMale DESC LIMIT 10")

#TODO finish implementing accuracy updates.
class WhoAmIStats(object):
    
    def __init__(self,wordlist = [], study_key):
        if len(wordlist) > 0:
            self.topMWords = self.__getWordlist(topMQuery)
            self.topFWords = self.__getWordlist(topFQuery)
            self.successRate = self.calcSuccess()
            #self.confidence = 0
            self.words = self.getUsedWords(wordlist)
        
    # TODO Calculates the confidence of the current prediction
    def __calcConfidence(self):
        #Need the probability values from the naiveAlgo...
        pass
    
    def __getWordlist(self,query,study_key):
        # Modify the query with the study in question
        
        results = dbUtils.execQuery(query)
        words = []
        for result in results:
            words.append(result[0])
        
        return words
            
    
    def calcSuccess(self, wordlist):
        if len(wordlist) < 1:
            return 0
        
        researchQs = set()
        for word in wordlist:
            researchQs.add(models.Word.objects.get(study = word.study))
            
        # Query the who am i research study
        if len(researchQs) == 1:
            researchQ = models.ResearchQuery.objects.get(study_title = researchQs[0])
            return round(researchQ.successes/(researchQ.fails + researchQ.successes)*100,1)
        elif len(researchQs) == 0:
            return 0
        else:
            # Create a dictionary of the research queries and their success
            successReports = {}
            for question in researchQs:
                researchQ = models.ResearchQuery.objects.get(study_title = question)
                successReports[question] = round(researchQ.successes/(researchQ.fails + researchQ.successes)*100,1)
            
            return successReports
            
            
    
    def getUsedWords(self,wrds):
        wordsUsed = []
        for word in wrds:
            wordsUsed.append(sqliteData.getWord(word))
        
        return wordsUsed
    