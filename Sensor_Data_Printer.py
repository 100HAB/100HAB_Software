# Import libreries that will be used in this script

import time 
import board
import adafruit_bme680
import adafruit_veml6070
import adafruit_ccs811
import gpsd
import csv



#Declare sensor names
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
veml6070 = adafruit_veml6070.VEML6070(i2c)
ccs811 = adafruit_ccs811.CCS811(i2c)


#Connect to the GPS daemon, started by MManager.sh
gpsd.connect()

#Wait for the CCS811 to be ready
while not ccs811.data_ready:
    pass

#Create a loop which will be running for 5 minutes
for i in range(0,300):
    #Get the actual sensor data.
    gps = gpsd.get_current()
    bdtime = time.strftime("%H%M%S")
    temp = bme680.temperature
    humity = bme680.humidity
    pressure = bme680.pressure
    voc = bme680.gas
    uv = veml6070.uv_raw
    co2 = ccs811.eco2
    tvoc = ccs811.tvoc

    print("{0}, {1:.3f}, {2:.3f}, {3:.3f}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}".format(bdtime, temp, humity, pressure, voc, uv, co2, tvoc, gps.lat, gps.lon, gps.alt, gps.mode, gps.sats))
    #Increase the i to indicate the actual iteration
    i = i+1
    #Wait a second before continuing
    time.sleep(1)

#Shut down the program once the loop is finished
exit()
