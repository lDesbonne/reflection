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

# Flag to check if new studies have been loaded
initialized = False

# Initialize global INFO
def initGlobalData():
    # Get all approved topic areas
    try:
        approvedAreas = TopicAreas.objects.filter(status=True)
        
        approvedStudies = ResearchProposals.objects.filter(status=True)
        
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
        
        initialized = True
    except Exception:
        initialized = True

def newTopic(title, detail, alias=None, status=False):
    topic = TopicAreas(topic_area=title, detail=detail, status=status, alias=alias)
    topic.save()

def evaluateTopic(title, detail, alias):
    novelTopic = True
    # Check to see if its an approved topic
    if (len(liveTopicAreas) > 0):
        for liveTopic in liveTopicAreas:
            if liveTopic == title:
                novelTopic = False
                return True
    if novelTopic:
        # Check to see if its in the database already
        try:
            TopicAreas.objects.get(topic_area=title)
            novelTopic = False
            #Topic already exists in the database
            return True
        except TopicAreas.DoesNotExist:
            try:
                newTopic(title, detail, alias)
                return True
            except Exception:
                # Cant add new topic
                return False
            
def newResearchQuery(title, detail, topic, status=False, alias=None):
    # check that the topic exists
    associatedTopic = TopicAreas.objects.get(topic_area=topic)
    if associatedTopic != None:
        res = ResearchProposals(proposal=title, detail=detail, topic=associatedTopic, status=status, alias=alias)
        res.save()

def evaluateResearchQuery(question, qAlias, qDetail, topic):
    newStudy = True
    # Check to see if the question exists for the topic
    if liveTopicsStudies.get(topic) != None:
        associatedStudies = liveTopicsStudies[topic]
        for aStudy in associatedStudies:
            if aStudy == question:
                newStudy = False
                break
    else:
        # Check in the database for this question in non approved status
        try:
            proposals = ResearchProposals.objects.filter(topic=TopicAreas.objects.get(topic_area=topic))
            for proposal in proposals:
                if proposal.proposal == question:
                    newStudy = False
                    return newStudy
        except Exception:       
            if newStudy:
                try:    
                    newResearchQuery(title=question, detail=qDetail, topic=topic, alias=qAlias)   
                    return newStudy
                except Exception:
                    # Failed to process new query
                    return False
                       

def approveTopic(topic):
    if TopicAreas.objects.get(topic_area=topic) != None:
        topic = TopicAreas.objects.get(topic_area=topic)
        topic.status = True
        topic.save()
        initialized = False

def approveResearchQuery(query_name):
    if ResearchProposals.objects.get(proposal=query_name) != None:
        prop = ResearchProposals.objects.get(proposal=query_name)
        prop.status = True
        prop.save()
        initialized = False

