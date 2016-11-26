'''
Created on 28 Oct 2016

Contains functions that provide statistical information 
regarding the "Who Am I?" project.

@author: Lennon
'''

from whoAmI.database import dbUtils, sqliteData
from numpy import array

#Query for top 10 words used by woman
topFQuery = "SELECT * FROM whoAmI_word ORDER BY cMale DESC LIMIT 10"
#Query for top 10 words used by men
topMQuery = "SELECT * FROM whoAmI_word ORDER BY cFem DESC LIMIT 10"
#Holds up to 100 of the previous guesses
guesses = []

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
    def calcSuccess(self,success=-1):
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
    
    def getUsedWords(self,wrds):
        wordsUsed = []
        for word in wrds:
            wordsUsed.append(sqliteData.getWord(word))
        
        return wordsUsed
    