import os 
import shutil

source=input('ENTER THE FILE NAME') 
destination=input('ENTER UR DESTINATION VALUE')
source=source+"/"
destination=destination+"/"

files=os.listdir(source)
for i in files :
    shutil.move((source+i),destination)