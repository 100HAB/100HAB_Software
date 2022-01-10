#Import all the libraries that will be used in this script
import subprocess
import time
import sys
import os

#Declare Instance number
Instance = 1

#Start the loop that will run the recollector script once every 5 minutes (10 seconds for starting)
while True:
  subprocess.call('python3 /home/pi/Sensor_Data_Recollector.py', shell=True)
  print("Running Instance:" + Instance)
  Instance = Instance + 1
  time.sleep(310)
