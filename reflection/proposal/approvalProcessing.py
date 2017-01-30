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

# Dictionary of topics and studies
liveTopicsStudies = {}

# Flag to check if application has been restarted
initialized = False

# Initialize global INFO
def initGlobalData():
    # Get all approved topic areas
    approvedAreas = TopicAreas.objects.get(status = True)
    
    approvedStudies = ResearchProposals.objects.get(status = True)
    
    for area in approvedAreas:
        liveTopicAreas.append(area.topic_area)
    
    # Get all approved studies
    for study in approvedStudies:
        liveStudies[study.proposal] = study.topic 
    
    studies = liveStudies.keys()
    for topic in TopicAreas:
        topicStudies = []
        for study in studies:
            if liveStudies.get(study) == topic:
                topicStudies.append(study)
    
        liveTopicsStudies[topic] = topicStudies

# 
def newTopic(title, detail, status = False):
    topic = TopicAreas(title, detail, status)
    topic.save()
    pass

def newResearchQuery(title, detail, topic, status = False):
    # check that the topic exists
    if TopicAreas.objects.get(topic_area = topic) != None:
        res = ResearchProposals(title, detail, topic, status)
        res.save()

def approveTopic(topic):
    if TopicAreas.objects.get(topic_area = topic) != None:
        topic = TopicAreas.objects.get(topic_area = topic)
        topic.status = True
        topic.save()


def approveResearchQuery(query_name):
    if ResearchProposals.objects.get(proposal = query_name) != None:
        prop = ResearchProposals.objects.get(proposal = query_name)
        prop.status = True
        prop.save()

