'''
Contains investigative methods for approving topics and
research questions

Created on 29 Jan 2017

@author: Lennon
'''
from reflection.models import TopicAreas
from reflection.models import ResearchProposals

# List of approved topics
liveTopicAreas = []

# Dictionary of topics and associated studies
liveStudies = {}

# Flag to check if application has been restarted
initialized = False

# Initialize global INFO
def initGlobalData():
    # Get all approved topic areas
    
    
    # Get all approved studies
    pass

# 
def newTopic(title, detail, status = False):
    
    pass

def newResearchQuery(title, detail, topic, status = False):
    pass

def approveTopic(topic):
    pass


def approveResearchQuery(query_name):
    pass


