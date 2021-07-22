# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:29:02 2018

@author: Kim
"""
from win32api import GetSystemMetrics
import os

#SUBJECT = easygui.enterbox(msg = "Enter subject number: ")

# Specify where you want the data stored
#DIRECTORY = 'yourpath'

# Or get it automatically from the current working directory
DIRECTORY = os.getcwd()

# Display properties

# Specify it manually
#DISPSIZE = (1366, 768)

# Or automatically
DISPSIZE = (GetSystemMetrics(0), GetSystemMetrics(1))
DISPTYPE = 'psychopy'
 
# Eye tracker properties
TRACKERTYPE = 'opengaze'

# Background color black
BGC = (0,0,0)

# Foreground color grey
FGC = (122, 122, 122)

# input subject number
#LOGFILENAME = DIRECTORY + '\Eye data\pvt_eye_' + SUBJECT
#LOGFILE = LOGFILENAME

#LOG_BEH = DIRECTORY + SUBJECT

# Trials per block
# BLOCKLENGTHS = [100]

