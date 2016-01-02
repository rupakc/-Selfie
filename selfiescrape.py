# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 20:29:44 2016
TODO - Add a better Timer or scheduler
@author: Rupak Chakraborty
"""
from bs4 import BeautifulSoup 
import urllib
import os 
import time
from threading import Timer

url = "http://selfeed.com/"

if not os.path.isdir('Selfie'):
    os.mkdir("Selfie")

os.chdir("Selfie")
c = 1

def saveFile(url,filename):
    urllib.urlretrieve(url,filename)  
    
def downloadSelfies():  
    
    global c
    webPage= urllib.urlopen(url).read()
    soup = BeautifulSoup(webPage)
    selfie_list = soup.find_all(name='div',attrs={"class":"selfie"})
    selfie_links = list([])  
    selfie_formats = list([]) 
    
    for selfie in selfie_list:
        link =  selfie["style"]
        start_index = link.find("https://")
        if start_index != -1:
            end_index = link.find(")",start_index+1)
        if end_index != -1:
            image_link = link[start_index:end_index]
            selfie_links.append(image_link.strip())
    
    for link in selfie_links:
        start_index = link.find("_n")
        if start_index != -1:
            end_index = link.find(".",start_index+1)
            if end_index != -1:
                image_format = link[end_index:]
                selfie_formats.append(image_format.strip())
    
    start = time.time()
    print "Starting downlaod of selfies ..." 
    
    for image_link,image_format in zip(selfie_links,selfie_formats):
        save_filename = str(c) + image_format
        saveFile(image_link,save_filename)
        c = c + 1 
        
    end = time.time()
    
    print "Time Taken to download Selfies : ", end-start
    print "Total Selfie Count : ", c 
    
    time.sleep(70)

while True:
    downloadSelfies()
    
