'''
Created on 21 Oct 2016
Urls for the Who Am I study

@author: Lennon
'''

from django.conf.urls import urlfrom genPerGen import views as gpg
app_name = 'genPerGen'
urlpatterns = [
    url(r'^data/',gpg.dataIn,name='dataIn'),
    url(r'^results/',gpg.predictGender,name='results'),
    url(r'^breakdown/',gpg.breakdown,name='breakdown'),
]
