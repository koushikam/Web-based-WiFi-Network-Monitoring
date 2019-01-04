#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 00:12:08 2017

@author: koushik
"""
import sys
import subprocess as s
import re 
import numpy as np
import json
from operator import itemgetter





def wifi_scan(): # wifi scanning using iwlist command
    def matching(search,line):
        return re.search(search,line) # re.search('Address: (\S+)',line)# 

    proc =  s.Popen('iwlist scan 2>/dev/null', shell=True, stdout= s.PIPE, ) 
    stdout_str = proc.communicate()[0] 
    stdout_list = stdout_str.split('\n') 
 
    Search= np.array(['Address: (\S+)'])
    Search = np.append(Search,'ESSID:"(\S+)"')
    Search = np.append(Search,'Quality=([0-9]+)\/([0-9]+)[ \t]+Signal level=([0-9-]+) dBm')
    Search = np.append(Search,'Encryption key:(on|.+)')
    Search = np.append(Search,'Channel:([0-9]+)')
    Search = np.append(Search,'Frequency:([0-9\.]+) GHz')

    APs = [] # Grouping all the APs details
    AP = {} # Collecting AP's details

    for line in stdout_list:
        line = line.strip()
        match = matching(Search[0],line) # re.search('Address: (\S+)',line)# 
    
        if match:
            if len(AP):
                APs.append(AP)
                AP={}
                AP["BSSID/MAC"] = match.group(1)
        
        match = matching(Search[1],line) #  re.search('ESSID:"(\S+)"',line)# 
        if match:
            AP["SSID"] = match.group(1)
     
        # Signal Quality and Power level
        match = matching(Search[2],line)
        if match:
            AP["Quality"] = float(match.group(1))
            AP["Quality_scale"] = float(match.group(2))
            AP["Power[dBm]"] = float(match.group(3))
         
            # Encryption key Status
            match = matching(Search[3],line)# re.search('Encryption key:(on|.+)',line)
            if match:
                AP["Encryption"] = match.group(1)
     
        # Channel being used
        match = matching(Search[4],line) #re.search('Channel:([0-9]+)',line)
        if match:
            AP["Primary Channel"] = float(match.group(1))
         
            # Channel Frequency
        match = matching(Search[5],line) #re.search('Frequency:([0-9\.]+) GHz',line)
        if match:
            AP["Freq"] = float(match.group(1))
     
   

    if len(AP):
        APs.append(AP) 

    APs = sorted(APs, key=itemgetter('Quality'),reverse=True)
    
    return json.dumps(APs),len(APs) # Json data
