#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import cv2
import glob
import os
import sys
import random
import numpy as np
import glob
#from glob import glob
import shutil
from tqdm import tqdm
import pathlib
import re
path='H:/all_remove_reflection'
#path='I:/IRIS DATASET/ORIIIIIIIIIIGINAL/ubiris2_1/CLASSES_400_300_Part1'
pathright='H:/ubl'
pathleft='H:/ubr'

for img in os.listdir(path):
    pathimage=os.path.join(path,img)
    
    #pathwrite=os.path.join(path3)
    print("img:",img)
    split = re.split('_+',img)
    print(split)
    print(split[0])
    split2=split[0]
    split2=split2[1:]
    print("split2:",split2)
    
    if int(split2)%2==0:
        
        pathwrite=os.path.join(pathright,split2)
        if not os.path.exists(pathwrite):
            os.mkdir(pathwrite)
        pathwriteimg=os.path.join(pathwrite,img)
        shutil.copy(pathimage,pathwriteimg)
    
    else:
        pathwrite=os.path.join(pathleft,split2)
        if not os.path.exists(pathwrite):
            os.mkdir(pathwrite)
        pathwriteimg=os.path.join(pathwrite,img)
        shutil.copy(pathimage,pathwriteimg)
      
        
    
    
    
    


# In[ ]:




