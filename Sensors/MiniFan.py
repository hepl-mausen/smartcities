#File : Mini fan
#making an intelligent fan
#loic.mausen@student.hepl.be

#copy only the part you want to try

### Turning ON the fan while pressing the button ###

from machine import Pin                                 #import function from library

button = machine.Pin(16, machine.Pin.IN)                #define the pin 16 as an input and name it button
fan = machine.Pin(18, machine.Pin.OUT)                  #define the pin 18 as an output and name it fan  


while True:                                             #starting the while loop
    val = button.value()                                #get the button value and naming it val 
    if val == 1:                                        #if val = 1
        fan.value(1)                                    #start the fan by putting the pin on 1
    else:                                               #else
        fan.value(0)                                    #put the pin of the fan to 0 
        
    
    
### Turning ON/OFF the fan while pressing the button ###   

from machine import Pin                                 #import function from library
from utime import sleep_ms

button = machine.Pin(16, machine.Pin.IN)                #define the pin 16 as an input and name it button
fan = machine.Pin(18, machine.Pin.OUT)                  #define the pin 18 as an output and name it fan
val = 0                                                 #set the value of val to 0

while True:                                             #start the while loop 
    val = button.value()                                #get the button value and naming it val 
    if val == 1:                                        #if val = 1  
        fan.toggle()                                    #change the value of the pin of the fan 
        sleep_ms(200)                                   #wait 200 ms
        
        
### intellingent fan ###
        
from lcd1602 import LCD1602                             #import function from library
from dht11 import *
from machine import I2C, Pin, ADC
from utime import sleep_ms

i2c = I2C(1, scl=Pin(7), sda = Pin(6), freq = 400000)   #define the pins for I2C
d =  LCD1602(i2c, 2, 16)                                #label data type, number of lines and characters per line
d.display()                                             #enable display
dht = DHT(16)                                           #set the pins of the dht11
fan = machine.Pin(18, machine.Pin.OUT)                  #define the pin 16 as an output and name it fan

while True:                                             #starting the while loop
    temp = dht.readTemperature()                        #get the temperature with the dht11
    sleep_ms(200)                                       #wait 200ms
    d.clear()                                           #clear what's on the screen 
    d.setCursor(0,0)                                    #set cursor 
    d.print("Temp:" +str(temp))                         #turn the 'temp' value in a string and print it on the screen
    sleep_ms(200)                                       #wait 200 ms
    if temp > 23:                                       #if the temperature is above 23
        fan.value(1)                                    #start the fan by sending 1 on its pin
    else:                                               #else
        fan.value(0)                                    #stop the fan by sending 0 on its pin 