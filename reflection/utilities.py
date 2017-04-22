'''
Created on 2 Oct 2016

@author: Lennon

Contains utility functions to be used throughout the project
'''
import json
from reflection.proposal import approvalProcessing
#Returns alternative correct spelling suggestions
def spellCheck(word):
    return []

#Evaluates if this is a real word
def isEnglishWord(word):
    return True

#Saves proposals
def storeProposal(proposal):
    #TODO improve the information returned from the save process
    #topicExists = "Saved with existing topic"
    #queryExists = "Query already exists in the database"
    #Check if topic exists
    topicSaved = approvalProcessing.evaluateTopic(proposal['topic_area'], proposal['topic_detail'], proposal['topic_alias']) 
    if approvalProcessing.evaluateResearchQuery(proposal['question'], proposal['question_alias'], proposal['question_detail'], proposal['topic_area']):
        if topicSaved:
            return True
        return True
    else:
        return False

#Investigates the existence of similar questions
def similarQuestions(hypothesis):
    suggestions = []
    return suggestions
