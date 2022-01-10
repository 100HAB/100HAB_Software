#Print a text indicating the script is running

echo "Script started, waiting 5 seconds before continuing"
sleep 5

#Execute Direwolf in a screen session
screen -dmS direwolf direwolf 
echo "Direwolf started, waiting 5 seconds before starting everything"

#Start the GPS Daemon
gpsd /dev/ttyS0
echo "GPS started and connected"

#create a screen session with SD_Instance_man.py
screen -dmS SD_MAN python3 SD_Instance_man.py
echo "Started recollecting Sensor Data"

#Declare Instance variable to indicate capture number
Instance=1
declare -i Instance

#Loop the Camera script, once each 5 minutes
while true; do
#create a screen session with Raspberry Pi Camera
screen -dmS Cam bash RPC_Record.sh
echo "Finished loading. 5 Minutes before reloading. Recording number $Instance"
Instance+=1
sleep 310

done

