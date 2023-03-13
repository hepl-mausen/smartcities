#File : Button
#Turning on/off a led with a button 
#loic.mausen@student.hepl.be

#copy only the part you want to try


### turning the led ON with the button ###

import machine                                    #import the libraries
button = machine.Pin(16, machine.Pin.IN)          #define pin 16 as an input and name it "button"
led = machine.Pin(18, machine.Pin.OUT)            #define pin 18 as an output and name it "LED"

while True:                                       #starting the while loop
    val = button.value()                          #putting the button value in the variable "val"
    if val == 1:                                  #if the value of val is 1
        led.value(1)                              #turn the led ON
    else:                                         #else
        led.value(0)                              #turning the led OFF


        
### switching led mode with the button ##

import machine                                    #import the libraries
import utime

button = machine.Pin(16, machine.Pin.IN)          #define pin 16 as an input and name it "button"
led = machine.Pin(18, machine.Pin.OUT)            #define pin 16 as an output and name it "LED"

val = 0                                           #setting the value of val on 0

while True:                                       #starting the while loop
    if button.value() == 1:                       #if the button value is 1
        val = val + 1                             #increment val by 1
        utime.sleep_ms(500)                       #stops the program for 1 sec
        
    elif val == 2:                                #else if val is 2
        val = 0                                   #set val on 0
         
    led.value(val)                                #putt the value of val on the led pin (turning it ON or OFF)