#File : Blinking led 
#making led blink with for and while loops 
#loic.mausen@student.hepl.be

#copy only the part you want to try 


### blink with for loop ###

import machine										#import the libraries
import utime
LED = machine.Pin(16,machine.Pin.OUT)               #define pin 16 as an output and name it "LED"

for i in range (10):                                #starting the for loop
    LED.value(1)                                    #setting the led pin value on 1 (turning it on)
    utime.sleep_ms(1000)                            #stops the program for 1 sec
    LED.value(0)                                    #setting the led pin value on 0 (turning it OFF)
    utime.sleep_ms(1000)                            #stops the program for 1 sec
    

    
### blink with while loop ###
    
import machine                                      #import the libraries
import utime
LED = machine.Pin(16,machine.Pin.OUT)               #define pin 16 as an output and name it "LED"

while True :                                        #starting the while loop 
    LED.value(1)                                    #setting the led pin value on 1 (turning it on)
    utime.sleep_ms(1000)                            #stops the program for 1 sec
    LED.value(0)                                    #setting the led pin value on 0 (turning it OFF)
    utime.sleep_ms(1000)                            #stops the program for 1 sec