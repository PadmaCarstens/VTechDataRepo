# -*- coding: utf-8 -*-
"""
Created on Fri Jul 4 12:30:24 2023

@author: padma carstens
"""
"""
Purpose: 
-Runs the aptrust command-line utility (apt-cmd, partner tools) at https://aptrust.github.io/userguide/partner_tools/ to read registry list on aptrust
-Returns '0' if file/object identifier is present in the registry' or '1' if the file/object identifier is not present in the registry
-Returns '0' if registry request to aptrust fails
"""
import json
import sys
import subprocess
import os
from subprocess import Popen, PIPE
#Get the parameters from configurations.ini to retrieve folder path settings
import configparser
config=configparser.RawConfigParser()
config.read('configurations.ini')

def registryCheck(bagName):
  os.environ['APTRUST_AWS_KEY']=config["APTrustSettings"]["AWSkey"]
  os.environ['APTRUST_AWS_SECRET']=config["APTrustSettings"]["AWSsecret"]
  os.environ['APTRUST_REGISTRY_API_KEY']=config["APTrustSettings"]["registryKey"]
  os.environ['APTRUST_REGISTRY_API_VERSION']=config["APTrustSettings"]["registryAPIversion"]
  os.environ['APTRUST_REGISTRY_EMAIL']=config["APTrustSettings"]["registryEmail"]
  os.environ['APTRUST_REGISTRY_URL']=config["APTrustSettings"][ "registryURL"]
  platformExt=config["APTrustSettings"]["platformExtn"]
  cmd=platformExt+"apt-cmd registry get object identifier=vt.edu/"+bagName
  child = subprocess.Popen(cmd, shell=True,  stderr=subprocess.PIPE, stdout=subprocess.PIPE,close_fds=True,encoding='utf8')
  stdout_data, stderr_data = child.communicate()
  
  if child.returncode == 1:
    print("**************************REGISTRY REQUEST FOR THE BAG FAILED, PLEASE CHECK YOUR AP TRUST REGISTRY CREDENTIALS AND TRY AGAIN**************************************************")
    #break
    return 0
  else:     
    stdString=json.loads(stdout_data)
    stdOut=json.dumps(stdString)
    if stdOut.startswith('{"error"'):
      print('Filename (object identifier): '+bagName+' is not found in APTrust bag registry in repo, so uploading this bag to APtrust')
      return 1
    elif child.returncode==0:
      print("*************************************************")
      print("****Bag: "+bagName+" already exists in aptrust bag registry***")
      print("*************************************************")
      overWriteBag=input("DO YOU WANT TO OVERWRITE THE EXISTING BAG? (yes/no) ")
      if overWriteBag == 'yes':
       print('You picked to overwrite the bag')
       return 1
      elif overWriteBag =='no':
        print('You picked to keep the existing copy of the bag: '+bagName+' in aptrust repo bag and terminate this upload process to overwrite the existing bag')
        return 0
      else:
        print('Type yes or no')
                       
    #if stdout_data is not None:
    #  print(stdout_data)
  
# Example run:
#x=registryCheck("VTDR_I00XYZ_CarstensP_CarstensP_v01_20230119")
#x=registryCheck("VTDR_P00257_I00289_DOI_23741097_ShirzaeiM_v01_20230726")

#print("return code is x = ",x)