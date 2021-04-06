# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:39:43 2021

Program to access set of presidential speeches by name or number

@author: eachr
"""


import db_ec
import sqlite3
import pandas as pd

class PresidentialAccess:
    
     def __init__(self, number, target_db, name = None, regex_match):
        import os
        self.name = name
        self.number = int(number)
        self.db_loc = target_db
        self.regex_match  = regex_match
        
        
     def countSpeeches(self):
        statement = "SELECT COUNT(*) FROM speeches WHERE PresidentName = %s" %(self.name)
        
        try:
            conn = edbd.connect_db(db_loc)
            cur = conn.cursor()
            
            cur.execute(statement)
            
        except:
            print("Error counting speeches")
            
        finally:
            res = cur.fecthall()
            
            