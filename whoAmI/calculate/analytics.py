'''
Created on 28 Oct 2016

Contains functions that provide statistical information 
regarding the "Who Am I?" project.

@author: Lennon
'''

from whoAmI.database import dbUtils, sqliteData
from whoAmI import models
from numpy import array

#Query for top 10 words used by woman
topFQuery = "SELECT * FROM whoAmI_word WHERE cFem != 0 ORDER BY cFem DESC LIMIT 10"
#Query for top 10 words used by men
topMQuery = "SELECT * FROM whoAmI_word WHERE cMale != 0 ORDER BY cMale DESC LIMIT 10"
#Holds up to 100 of the previous guesses
guesses = []

#TODO finish implementing accuracy updates.
class WhoAmIStats(object):
    
    def __init__(self,wordlist = []):
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
    
    def __getWordlist(self,query):
        results = dbUtils.execQuery(query)
        words = []
        for result in results:
            words.append(result[0])
        
        return words
            
    #Calculates the success rate based on the 
    def calcSuccessOld(self,success=-1):
        if success > -1 and success <= 1:
            if len(guesses) < 100:
                guesses.append(success)
            elif len(guesses) == 100:
                guesses.pop(0) #Remove the 1st object in the list
                guesses.append(success)
        
        if len(guesses) > 0:
            guessArray = array(guesses)
            return (sum(guessArray)/len(guesses))*100
            
        else:
            return 0
    
    def calcSuccess(self):
        # Query the who am i research study
        researchQ = models.ResearchQuery.objects.get(study_title = 'whoAmI')
        return round(researchQ.successes/(researchQ.fails + researchQ.successes)*100,1)
            
            
    
    def getUsedWords(self,wrds):
        wordsUsed = []
        for word in wrds:
            wordsUsed.append(sqliteData.getWord(word))
        
        return wordsUsed
    