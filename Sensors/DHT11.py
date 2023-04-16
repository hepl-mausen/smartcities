#File : DHT11
#temperature and humididty monitoring
#loic.mausen@student.hepl.be

#copy only the part you want to try


### Display temperature and humidity on LCD ###

from lcd1602 import LCD1602                                  #import functions from libraries
from dht11 import *
from machine import I2C, Pin, ADC
from utime import sleep_ms

i2c = I2C(1, scl=Pin(7), sda = Pin(6), freq = 400000)        #define the pins for I2C
d =  LCD1602(i2c, 2, 16)                                     #label data type, number of lines and characters per line 
d.display()                                                  #enable display 
dht = DHT(18)                                                #set the pins of the dht11

while True:
    
    temp, humid = dht.readTempHumid()                        #get the temperature and humidity 
    sleep_ms(1000)                                           #wait 1000 ms
    d.clear()                                                #clear what's on the screen
    d.setCursor(0,0)                                         #set the cursor of the lcd
    d.print("Temp :" +str(temp))                             #turn the 'temp' value in a string and print it on the screen 
    d.setCursor(0,1)                                         #set the cursor of the lcd
    d.print("Humid :" +str(humid))                           #turn the 'humid' value in a string and print it on the screen 
    sleep_ms(1000)                                           #wait 1000 ms
    
    
    
### Display temperature and humidity on LCD with alarm ### 

from lcd1602 import LCD1602                                  #import functions from libraries
from dht11 import *
from machine import I2C, Pin, ADC, PWM 
from utime import sleep_ms

i2c = I2C(1, scl=Pin(7), sda = Pin(6), freq = 400000)        #define the pins for I2C
d =  LCD1602(i2c, 2, 16)                                     #label data type, number of lines and characters per line
d.display()                                                  #enable display
dht = DHT(18)                                                #set the pins of the dht11
buzzer = PWM(Pin(16))                                        #setting the pin 18 as an PWM output an naming it buzzer

while True:
    temp, humid = dht.readTempHumid()                        #get the temperature and humidity     
    sleep_ms(1000)                                           #wait 1000 ms
    d.clear()                                                #clear what's on the screen
    d.setCursor(0,0)                                         #set the cursor of the lcd
    d.print("Temp : " +str(temp))                            #turn the 'temp' value in a string and print it on the screen 
    d.setCursor(0,1)                                         #set the cursor of the lcd
    d.print("humid : " +str(humid))                          #turn the 'humid' value in a string and print it on the screen 
    sleep_ms(1000)                                           #wait 1000 ms
    if temp > 22 or humid > 40:                              #if temp is above 22 or humid above 
        buzzer.freq(1000)                                    #set the frequence of the buzzer to 1000
        buzzer.duty_u16(1000)                                #set the buzzer duty cycle on 1000
    else:
        buzzer.duty_u16(0)                                   #else set it to 0 s
        
            