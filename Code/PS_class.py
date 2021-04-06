# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:42:30 2021

@author: eachr
"""

import db_ec
import sqlite3
import pandas as pd
import re

class PS:
    '''
    Class defined to process a single speech
    Methods can be called to return various aspects of the speech or just return the speech
        in one of two ways
            1) Unstructured - dictionary of speaker and list of all sentences spoken at speech
            2) Strucutred - 
    '''
    
    def __init__(self, text, President ,speech_id):
        import os
        self.text = text
        self.President = President
        
        
    def get_tag_type(self):
        return "Test"

    def get_speech(self):
        
        from nltk.tokenize import sent_tokenize
        
        ##REturn speech where president is only speaker (untagged)
        with open (self.text,'r', encoding='utf-8') as doc:
            title =  doc.readline() #first line formatted title
            date  = doc.readline() #second line formatted date
            speech = doc.readlines() # rest the speech
            
         #Parse speech for sentence tokenization 
        ## < > used to tag Applause, etc.
        sentences = sent_tokenize("".join(speech))        
        speech_dict = {'Name':title, 'Date':date,'Speech': sentences}
        
        return speech_dict
    
    def read_in_01(self):
        import re
        '''
        Tags in \speeches use SPEAKER TITLE/NAME: to denote speakers, while non-speech events are
        denoted with 
        
        Returns
        -------
        speech_dict - dictionary with speaker name as key and list of 

        '''
        
        
        #Caputre speaker tag patterns
        name_tag = r"([A-Z]+:)"
        #Full untterance tag
        utterance_tag = "([A-Z]+:).*"
        
        
        ## Tag speeches with end tags
        speech = "\n".join(self.text)       
        
        #find speaker tag by names
        
        speakers = set()
        ## loop defines all speakers in a speech
        for name in re.finditer(name_tag, speech):
            s = name.start()
            e = name.end()
            
            #Negative look behind to see if Vice president should be matched
            if re.search("(?<=\b(?:vice |v ))president",speech[s:e].lower() ):
                #IF it it president, tag as President name
                speaker_format = "self.President"
            else:
                #Format other speaker name
                speaker_format = speech[s:e].replace("<","").replace(">","").strip().lower()
            speakers.add(speaker_format)
        
        #=== dictionary of speaker, utterances (k,v)
        # initialize dictionary
        speech_dict = dict.fromkeys(speakers,[])
        
        #search
        for speaker in speakers:
            
            #speak
            
            utterances = re.compile("".join([speaker,".*"])).findall(speech)
                
            speech_dict[speaker_format] = utterances             
            
            
        
        
        
        
        
    
    def parseSpeech(self,speech):
        from nltk.tokenize import sent_tokenize
        
        speech = self.read_in()
        
        

        