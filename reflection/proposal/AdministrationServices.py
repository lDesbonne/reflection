'''
Created on 20 May 2017

@author: Lennon
'''
from reflection.models import TopicAreas
from reflection.models import ResearchProposals

# Attempting to create the admin data using Objects

valididInitializationValues = ['Live', 'Pending']
        
class ApprovalData:
    def __init__(self, name, information, dbId):
        self.name = name
        self.children = []
        self.information = information
        self.dbId = str(dbId)
    
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
                    
    return dataTree
    
