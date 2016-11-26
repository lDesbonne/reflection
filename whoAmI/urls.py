'''
Created on 21 Oct 2016
Urls for the Who Am I study

@author: Lennon
'''

from django.conf.urls import url
from . import views as wai
app_name = 'whoAmI'
urlpatterns = [
    url(r'^data/',wai.dataIn,name='dataIn'),
    url(r'^results/',wai.predictGender,name='results'),
    url(r'^breakdown/',wai.breakdown,name='breakdown'),
]
