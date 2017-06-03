'''
Created on 20 May 2017

@author: Lennon
'''
from reflection.models import TopicAreas
from reflection.models import ResearchProposals

#Attempting to create the admin data using Objects

valididInitializationValues = ['Live', 'Pending']

class ApprovalData:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
    
    def __str__(self):
        return '{"name":'+self.name+',"children":'+self.children+'}'
            
        
#Meta data should be added here to provide supplementary info
class ApprovalInfo:
    def __init__(self, name):
        self.name = name
        self.size = "1"
    
    def __str__(self):
        return '{"name":"'+self.name+'","size":'+self.size+'}'
        

class ApprovalDataBuilder:
    def __init__(self, init):
        self.questions = []
        self.dataTree = None
        self.validInitializer = False
        self.topicNames = None
        self.dataSet = None
        self.studies = None
        self.initialiser = None
        for initValue in valididInitializationValues:
            if initValue == init:
                self.validInitializer = True
                if initValue == 'Live':
                    self.active = True
                elif initValue == 'Pending':
                    self.active = False
                break
        
        if self.validInitializer:
            self.initialiser = init
        else:
            raise Exception("Initializer: "+init+" invalid")
    
    def build(self):
        #Create parent data holder
        self.dataTree = ApprovalData(name=self.initialiser + ' Topics')
        
        #Get all the names of the topics using the active flag
        self.topicNames = TopicAreas.objects.filter(status=self.active)
        
        #Create objects for those topics
        for topic in self.topicNames:
            #Get all of the studies with the flag for those topics
            self.studies = ResearchProposals.objects.filter(status=self.active, topic=topic)
            #Add all the questions to the topic
            for question in self.studies:
                self.questions.append(ApprovalInfo(name=question.proposal))
            
            self.dataSet = ApprovalData(name=topic.topic_area)
            self.dataSet.children = self.questions

            #Add to the dataTree
            self.dataTree.children.append(self.dataSet)
                        
        return self
    