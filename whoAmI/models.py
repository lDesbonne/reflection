from django.db import models

class Word(models.Model):
    word = models.CharField(max_length = 50, primary_key=True)
    #Initialised to 1 to avoid multiply by 0 in naive bayes
    cFem = models.IntegerField(default=0)
    cMale = models.IntegerField(default=0)
    
    def __str__(self):
        return self.word
    
    def details(self):
        cMale = str(self.cMale)
        cFem = str(self.cFem)
        return "{word:"+self.word+",classified male:"+cMale+",classified female:"+cFem+"}"

class ResearchQuery(models.Model):
    study_title = models.CharField(max_length = 200, primary_key=True)
    num_docs = models.IntegerField(default=0)
    successes = models.IntegerField(default=0)
    fails = models.IntegerField(default=0)
    
    def __str__(self):
        return self.study_title
    
    def details(self):
        return "{title:"+self.study_title+",number of entries:"+str(self.num_docs)+"}"
    
    def successRate(self):
        return self.successes/(self.successes + self.fails)*100
        
