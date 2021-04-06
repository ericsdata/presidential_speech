# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:31:27 2021

@author: eachr
"""

from PS_class_v2 import PS

tp = r"C:\Users\eachr\Documents\Projects\president_speeches\Data\trump\Trump008.txt"
tp2 = r"C:\Users\eachr\Documents\Projects\president_speeches\Data\Miller\Trump\test.txt"

lp = r"C:\Users\eachr\Documents\Projects\president_speeches\Data\lincoln\lincoln_speeches_005.txt"
name = "Trump"
ff = PS(tp2,name,"001")

gg = ff.get_speech()
PS