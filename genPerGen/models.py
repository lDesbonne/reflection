from django.db import models
from django.db.models.deletion import CASCADE
from reflection.models import ResearchProposals

STUDY_TITLE = "Gender Perception of Gender"
STUDY_ID = 1
STUDY_ALIAS = "genPerGen"
ASSOCIATED_STUDY = ResearchProposals.objects.get(id = STUDY_ID)

class Data(models.Model):
    study_title = models.ForeignKey(ResearchProposals, on_delete=models.CASCADE)
    num_docs = models.IntegerField("number of documents", default=0)
    successes = models.IntegerField("successful classifications", default=0)
    fails = models.IntegerField("false classifications", default=0)
    
    def __str__(self):
        return self.study_title
    
    def details(self):
        return "{title:"+self.study_title+",number of entries:"+str(self.num_docs)+"}"
    
    def successRate(self):
        return self.successes/(self.successes + self.fails)*100
        

class Word(models.Model):
    word = models.CharField(max_length = 50)
    #Initialised to 1 to avoid multiply by 0 in naive bayes
    cFem = models.IntegerField("classified Female", default=0)
    cMale = models.IntegerField("classified Male", default=0)
    
    def __str__(self):
        return self.word
    
    def details(self):
        cMale = str(self.cMale)
        cFem = str(self.cFem)
        return "{word:"+self.word+",classified male:"+cMale+",classified female:"+cFem+"}"
    