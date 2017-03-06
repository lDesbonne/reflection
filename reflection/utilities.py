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
    #Check if topic exists
    if approvalProcessing.evaluateTopic(proposal['topic_area'], proposal['topic_detail'], proposal['topic_alias']) and approvalProcessing.evaluateResearchQuery(proposal['question'], proposal['question_alias'], proposal['question_detail'], proposal['topic_area']):
        return True
    else:
        return False

#Investigates the existence of similar questions
def similarQuestions(hypothesis):
    suggestions = []
    return suggestions
