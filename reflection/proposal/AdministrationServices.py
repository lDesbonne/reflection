'''
Created on 20 May 2017

@author: Lennon
'''
from reflection.models import TopicAreas, ResearchProposals

# Attempting to create the admin data using Objects

valididInitializationValues = ['Live', 'Pending']
typeTopic = 'Topic'
typeQuestion = 'Question'
        
class ApprovalData:
    def __init__(self, name, information, dbId):
        self.name = name
        self.children = []
        self.information = information
        self.dbId = str(dbId)
        self.clickable = True
        
    def setClickable(self, clickable):
        self.clickable = clickable
    
    def __str__(self):
        return '{"name":' + self.name + ',"children":' + self.children + ', "detail":' + self.information + ', "id":'+self.dbId+'}'
            
        
# Meta data should be added here to provide supplementary info
class ApprovalInfo:
    def __init__(self, name, information, dbId):
        self.name = name
        self.size = "1"
        self.information = information
        self.dbId = str(dbId)
    
    def __str__(self):
        return '{"name":"' + self.name + '","size":' + self.size + ', "detail":"' + self.information + '", "id":'+self.dbId + '}'
        
class ProjectDataStructure(ApprovalData):
    def __init__(self, name, information):
        ApprovalData.__init__(self, name, information, "rootId")     

def approvalDataBuilder(initialiser):
    
    for initValue in valididInitializationValues:
        if initValue == initialiser:
            validInitializer = True
            if initValue == 'Live':
                active = True
            elif initValue == 'Pending':
                active = False
            break
    
    if not validInitializer:
        raise Exception("Initializer: " + initialiser + " invalid")
        
    # Create parent data holder
    dataTree = ProjectDataStructure(name=initialiser + ' Topics', information="root")
    
    if(active):
        # Get all the names of the topics using the active flag
        topicNames = TopicAreas.objects.filter(status=active)
        
        # Create objects for those topics
        for topic in topicNames:
            questions = []
            # Get all of the studies with the flag for those topics
            studies = ResearchProposals.objects.filter(status=active, topic=topic)
            # Add all the questions to the topic
            for question in studies:
                questions.append(ApprovalInfo(name=question.proposal, information=question.detail, dbId=question.id))
            
            dataSet = ApprovalData(name=topic.topic_area, information=topic.detail, dbId=topic.id)
            dataSet.children.extend(questions)
        
            # Add to the dataTree
            dataTree.children.append(dataSet)
    elif(not active):
        #Retrieve the questions first and match with all the topics
        pendingProposals = ResearchProposals.objects.filter(status=active)
        #Generate a list of all the topics
        topics = []
        for proposal in pendingProposals:
            topics.append(proposal.topic)
        associatedTopics = set(topics)
        
        for topic in associatedTopics:
            questions = []
            for question in pendingProposals:
                if (question.topic.id == topic.id):
                    questions.append(ApprovalInfo(name=question.proposal, information=question.detail, dbId=question.id))
            dataSet = ApprovalData(name=topic.topic_area, information=topic.detail, dbId=topic.id)
            if (topic.status):
                dataSet.setClickable(False);
            dataSet.children.extend(questions)
            
            #Add to the dataTree
            dataTree.children.append(dataSet)
                    
    return dataTree    
    
def applyUpdateToProjectData(dataId, dataStatus, dataType):
    #Success status of the update
    success = True
    try:
        if (dataType == typeTopic):
            #Update the topic table
            topic = TopicAreas.objects.filter(id = dataId)
            topic.update(status = bool(dataStatus))
            if (not bool(dataStatus)):
                #Deactivate all associated studies for that topic
                ResearchProposals.objects.filter(topic = topic.first()).update(status = bool(dataStatus))
            
        if (dataType == typeQuestion):
            #Update the question table
            proposal = ResearchProposals.objects.filter(id = dataId)
            proposal.update(status = bool(dataStatus))
            if (bool(dataStatus) and not proposal.first().topic.status):
                TopicAreas.objects.filter(id = proposal.first().topic.id).update(status = bool(dataStatus))
    except(Exception):
        success = False
        
    return success 

def loadPendingStudies():
    pendingStudyList = []
    pendingStudies = ResearchProposals.objects.filter(status = 0)
    for study in pendingStudies:
        pendingStudyList.append(str(study.id)+":"+str(study.topic_id))
    return pendingStudyList
