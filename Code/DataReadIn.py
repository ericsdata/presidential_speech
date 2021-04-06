# -*- coding: utf-8 -*-
"""
Speeches Data Read-in

BASED ON GRAMMAR LAB FOLDER AND FILE STRUCTURE

Created on Mon Jun 29 18:22:18 2020

@author: eachr
"""

import os
import sys
import re
import pandas as pd

abspath = os.path.abspath(__file__) #set wd to file location
dname = os.path.dirname(abspath)
os.chdir(dname)

import sqlite3
import db_ec
import datetime
from dateutil.parser import parse
from pandas import DataFrame

##init db

db_loc = "..\Data\Speeches.db"#location of DB
rootdir = "..\Data" #Location with president speeches arranged in named subdirectories

def create_db(db_loc):
    db_ec.create_db_connection(db_loc)
    
    speech_table = '''CREATE TABLE IF NOT EXISTS speeches(
                                PresidentName text,
                                SpeechName text,
                                SpeechDate text,
                                SpeechText text,
                                
                                primary key(PresidentName, SpeechName, SpeechDate)
                                );'''##Create table statemetn
    try:
        conn = db_ec.connect_db(db_loc)
        db_ec.create_table(conn, speech_table)
    except:
        print("Error creating table")
    finally:
        print("Speeches table created")
        conn.close()
        
def load_db():

    i = 0 #counter
    president_dict ={} ## Dictionary with president name as key, (speech_name, speech_date, speech_text)
    for subdir, dirs, files in os.walk(rootdir):
        #print(subdir)
        i += 1 
        if i == 1: #first subdirectory is rootdir itself - skip
            continue #skip top level folder
        for pNameLoc,m,files in os.walk(subdir):
            #print(pNameLoc)
            pName = pNameLoc.split("\\")[2] #extract presidents name from folder
            print("\nProcessing President",pName.capitalize())
            temp = []
            for file in files:
                fLoc = os.path.join(pNameLoc,file) #folder location
                with open(fLoc, encoding = "utf-8") as fp:
                    sTitle = fp.readline() #first line is title of speech
                    res = re.search('".*"', sTitle) #extract text between quotes
                    Title = re.sub('"','',res[0]) #remove quotes
                    
                    sDate = fp.readline() #second line is date
                    
                    if sDate =="\n": #double spaced file correction
                        sDate = fp.readline()
                        
                    res = re.search('".*"', sDate) #pull between quotes
                    Date = re.sub('"','',res[0]) #remove quotes
                    ##format date
                    date_time_obj = parse(Date).date()
                    DateF = date_time_obj.strftime("%Y-%m-%d")
                    
                    sText = fp.read() #read in full text corpus
                    
                    #formatting speeches
                    sTextF = re.sub(r"<.*>","",sText)#remove applause and laughter tags
                    sTextF = re.sub("\s+"," ",sTextF) #remove additional spaces
                    temp.append((pName,Title,DateF,sTextF))
                    
            president_dict[pName] = temp
            try:
                conn = db_ec.connect_db(db_loc)
                cur = conn.cursor()
                
                cur.executemany('''INSERT OR REPLACE into speeches(
                                                            PresidentName, 
                                                            SpeechName,
                                                            SpeechDate,
                                                            SpeechText)
                                    VALUES(?,?,?,?);''', temp)
                conn.commit()
            finally:
                conn.close()                              
                print("Processing President",pName.capitalize(),"Complete")
    return president_dict

def db_reader_dict(db_loc,stat):
    return_dict = {}
    try:
        conn = db_ec.connect_db(db_loc)
        cur = conn.cursor()
        cur.execute(stat)
        
        speeches = cur.fetchall()
        for speech in speeches:
            return_dict[(speech[0],speech[1],speech[2])] = speech[3]
            
    finally:
        return return_dict
        
def db_reader_pd(db_loc,stat):
  
  try:
      conn = db_ec.connect_db(db_loc)
      cur = conn.cursor()
      cur.execute(stat)
      
      df = DataFrame(cur.fetchall())
      df.columns = [ x[0] for x in cur.description ] 
          
  finally:
      return df      
  
# =============================================================================
# create_db(db_loc)
# g = load_db()
# stat = '''SELECT *
#           FROM Speeches
#           WHERE SpeechDate > "1969-01-19";'''
#           
#           
# all_nixon_on = db_reader(db_loc, stat)
# =============================================================================
