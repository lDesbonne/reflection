'''
Created on 2 Oct 2016

@author: Lennon

Contains the naive bayes classification algorithms for predicting
whether self describing words were chosen by males or females

'''
from numpy import *
from genPerGen.database import sqliteData

def classifyGender(wordlist):
    #remove words that are not in the database from the word list
    veriWordList, excList = wordlistVerifyer(wordlist)
    
    #probability of female and male classification, and probability of each 
    #word appearing
    probFem, probMal, probWordsF, probWordsM = calcProbClass(veriWordList)
    
    classifyFem = sum(probWordsF) + log(probFem)
    classifyMal = sum(probWordsM) + log(probMal)
    
    #TODO introduce a statistical significance parameter or confidence interval
    if (classifyFem > classifyMal):
        return 0, excList
    elif (classifyMal > classifyFem):
        return 1, excList
    else:
        return 2, excList

#Returns the probability
def calcProbClass(wordlist):
    #number of female classifications
    #Initialised to 2 to avoid divide by 0
    numberFem = 2 
    #number of male classifications
    numberMal = 2
    
    probEachWordF = [1]*5
    probEachWordM = [1]*5
    #wordAppear = []
    
    for word in sqliteData.getAllWords():
        numberFem += word.cFem
        numberMal += word.cMale
        
        for desc in wordlist:
            if (desc == word.word):
                if word.cFem > 0:
                    probEachWordF[wordlist.index(desc)] += word.cFem
                if word.cMale > 0:
                    probEachWordM[wordlist.index(desc)] += word.cMale
                #wordAppear.append(word.cFem + word.cMale)
                break
    
    #Check the size of the word probabilities
    #Every document should have 5 values
    if len(probEachWordF) != 5:
        #Find the placeholders for words not in the database
        for i in range(wordlist):
            if wordlist[i] == "NotPresent":
                #insert substitute values into the probability vector
                probEachWordF.insert(i,1)
                probEachWordM.insert(i,1)
                #wordAppear.insert(i,2)
                                
    probCMal = numberMal/(numberMal+numberFem)
    probCFem = numberFem/(numberFem+numberMal)
    #convert the python lists into numpy arrays
    
    totWordOccurrance = array(probEachWordF)+array(probEachWordM)
    probFMatrix = array(probEachWordF)/totWordOccurrance
    probMMatrix = array(probEachWordM)/totWordOccurrance
    
    #wordApp = array(wordAppear)/(numberFem+numberMal) #This value should be 1
    
    #Probability of a word occurring given a class
    probFMatrix = log(probFMatrix)
    probMMatrix = log(probMMatrix)
    
    return probCFem, probCMal,probFMatrix,probMMatrix

#Modifies the wordlist with a placeholder indicating missing word
def wordlistVerifyer(wordlist):
    #List of words that have not been found
    exclusions = []
    
    #Search for the existence of the word
    for i in range(len(wordlist)):
        if not sqliteData.queryWord(wordlist[i]):
            #Add the word to a list of not found words
            exclusions.append(wordlist[i])
            #Modify the wordlist with a placeholder
            wordlist[i] = "NotPresent"
        
    return wordlist, exclusions
    
            
        
        