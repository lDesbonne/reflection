'''
Created on 20 May 2017

@author: Lennon
'''
from reflection.models import TopicAreas
from reflection.models import ResearchProposals

# Attempting to create the admin data using Objects

valididInitializationValues = ['Live', 'Pending']
        
class ApprovalData:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def __str__(self):
        return '{"name":' + self.name + ',"children":' + self.children + '}'
            
        
# Meta data should be added here to provide supplementary info
class ApprovalInfo:
    def __init__(self, name):
        self.name = name
        self.size = "1"
    
    def __str__(self):
        return '{"name":"' + self.name + '","size":' + self.size + '}'
        
class ProjectDataStructure(ApprovalData):
    def __init__(self, name):
        ApprovalData.__init__(self, name)     

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
    dataTree = ProjectDataStructure(name=initialiser + ' Topics')
    
    # Get all the names of the topics using the active flag
    topicNames = TopicAreas.objects.filter(status=active)
    
    # Create objects for those topics
    for topic in topicNames:
        questions = []
        # Get all of the studies with the flag for those topics
        studies = ResearchProposals.objects.filter(status=active, topic=topic)
        # Add all the questions to the topic
        for question in studies:
            questions.append(ApprovalInfo(name=question.proposal))
        
        dataSet = ApprovalData(name=topic.topic_area)
        dataSet.children.extend(questions)

        # Add to the dataTree
        dataTree.children.append(dataSet)
                    
    return dataTree
    
