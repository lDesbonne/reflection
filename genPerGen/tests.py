from django.test import TestCase
from whoAmI.models import Word, Data
import genPerGen.calculate.naiveAlgo as classify
import genPerGen.database.dbUtils as util
import genPerGen.database.sqliteData as sDat
from numpy import *
from whoAmI.calculate import analytics

class WhoAmITest(TestCase):
    def setUp(self):
        
        #Populate database with document values
        #All values incremented by 1 to account for the default value of 1
        #Based on each document holding 5 unique descriptive words 
        Word.objects.create(word='beautiful',cFem=2)
        Word.objects.create(word='strong',cMale=3)
        Word.objects.create(word='bold',cMale=1,cFem=1)
        Word.objects.create(word='loner',cMale=1)
        Word.objects.create(word='lonely',cFem=1)
        Word.objects.create(word='assiduous',cMale=1,cFem=1)
        Word.objects.create(word='passionate',cMale=1,cFem=2)
        Word.objects.create(word='tall',cMale=3)
        Word.objects.create(word='lazy',cMale=1,cFem=1)
        Word.objects.create(word='loving',cFem=1)
        Word.objects.create(word='daring',cMale=3,cFem=1)
        Word.objects.create(word='extrovert',cMale=1,cFem=1)
        Word.objects.create(word='lanky',cFem=1)
        Word.objects.create(word='sporty',cMale=1,cFem=2)
        Word.objects.create(word='caring',cFem=2)
        Word.objects.create(word='ambitious',cMale=1,cFem=2)
        Word.objects.create(word='introvert',cMale=1)
        Word.objects.create(word='petite',cFem=1)
        Word.objects.create(word='musical',cMale=1)
        Word.objects.create(word='kind',cMale=2,cFem=2)
        Word.objects.create(word='friendly',cMale=1,cFem=1)
        Word.objects.create(word='happy',cMale=1,cFem=2)
        Word.objects.create(word='creative',cMale=1)
        Word.objects.create(word='dreamer',cMale=1,cFem=1)
        
        #Add the document type and number of entries to the database
        Data.objects.create(study_title='reflectionStudy_1',num_docs=1)
    
    def testClassifyFemale(self):
        #Create unit test to classify a female Document
        femDesc = ['beautiful','caring','petite','loving','happy']
        result, excList = classify.classifyGender(femDesc)
        self.assertTrue(result == 0, 'Female classification should return 0')
        
    def testClassifyMale(self):
        #Create a unit test to classify a male Document
        malDesc = ['strong','tall','musical','creative','loner']
        result, exclist = classify.classifyGender(malDesc)
        self.assertTrue(result == 1 , 'Male classification should return 1')
        
    
    def testWordNotPresentIdentification(self):
        #Test to see handling of words not in vocabulary
        selfDes = ['jovial','quaint','auspicious','creative','dreamer']
        wordList, exclusions = classify.wordlistVerifyer(selfDes)
        self.assertTrue(len(exclusions) == 3, 'Should contain 3 words not in the database')
        subsMade = False
        
        for i in range(len(wordList)):
            if wordList[i].__eq__("NotPresent"):
                subsMade = True
                break
        
        self.assertTrue(subsMade)
    
    def testDocSubission(self):
        #Tests adding new documents to the database
        cMal = 1
        cFem = 0
        
        numFBeaut = Word.objects.get(word="beautiful").cFem
        numFDream = Word.objects.get(word="dreamer").cFem
        exoticExists = sDat.queryWord("exotic")
        enigmatExists = sDat.queryWord("enigmatic")
        
        #Total number of words to begin with
        allWords = len(sDat.getAllWords())
        
        updateWords = ['beautiful','bold','loner','introvert','assiduous']
        updateNew = ['beautiful','exotic','shy','introvert','dreamer']
        allNew = ['enigmatic','extravagant','impulsive','influential','visionary']
        
        #Investigate update of existing words
        util.saveDocument(updateWords, cFem)
        newB = Word.objects.get(word="beautiful").cFem
        self.assertTrue(numFBeaut < newB, '1 more entry for beautiful expected')
        
        #Investigate an update and new words
        self.assertFalse(exoticExists, 'Exotic should not be present yet')
        util.saveDocument(updateNew,cFem)
        newD = Word.objects.get(word="dreamer").cFem
        self.assertTrue((numFDream < newD) and sDat.queryWord("exotic"),'Addition and increment of words')
        
        #Investigate addition of all new words
        self.assertFalse(enigmatExists, "Shold not be present yet")
        util.saveDocument(allNew, cMal)
        self.assertTrue(sDat.queryWord("enigmatic"), "Should now be present")
        
        #Investigate the total number of words now
        self.assertTrue(allWords < len(sDat.getAllWords()), "Should be more words in the database")
        
    def testStatGeneration(self):        
        #Initialize to 10 guesses with 7 correct
        analytics.guesses = [0,0,0,1,1,1,1,1,1,1]
        stats = analytics.WhoAmIStats()
        
        self.assertTrue(stats.calcSuccess() == 70, "Check that success history is read correctly")
        
        self.assertTrue(stats.calcSuccess(1) != 70, "Check that the success update works correctly")
        
        