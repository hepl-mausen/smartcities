#File : RotaryAngleSensor
#testing the rotary angle sensor
#loic.mausen@student.hepl.be

#uncomment the part you want to try



### testing the sensor ###

from machine import ADC                                          #import functions from libraries 
from utime import sleep

angle = ADC(0)                                                   #setting A0 as the ADC pin and naming it "angle"

while True:
    print(angle.read_u16())                                      #print the returnd value of the ADC pin (_u16 -> unsigned binary integer of up to 16 bits)
    sleep(1)                                                     #stops the program for 1sec 
                           
    
    
### Turning the led on/off with the sensor ###

from machine import ADC, Pin                                     #import functions from libraries
from time import sleep_ms 

led = Pin(16, Pin.OUT)                                           #define pin 16 as an output and name it "led"
sensor = ADC(1)                                                  #setting A1 as the ADC pin and naming it "sensor" 

while True:
    print(sensor.read_u16())                                     #print the returnd value of the ADC pin (_u16 -> unsigned binary integer of up to 16 bits)
    if sensor.read_u16() < 30000:                      
        led.value(1)                                             #turn the led ON if the value is higher than 30000
        sleep_ms(200)                                            #stops the program for 0.2sec 
    else:
        led.value(0)                                             #else, turn the led OFF
        sleep_ms(200)                                            #stops the program for 0.2sec
        
        
        
### Turning the led ON between 2 values ###

from machine import ADC, Pin                                     #import functions from libraries
from time import sleep_ms

led = Pin(16, Pin.OUT)                                           #define pin 16 as an output and name it "led"
sensor = ADC(1)                                                  #setting A1 as the ADC pin and naming it "sensor"

while True:
    print(sensor.read_u16())                                     #print the returnd value of the ADC pin (_u16 -> unsigned binary integer of up to 16 bits)
    if sensor.read_u16() > 20000 and sensor.read_u16() < 45000:
        led.value(1)                                             #if the value is between 20000 and 45000, turn the led ON
        sleep_ms(200)                                            #stops the program for 0.2sec
    else:
        led.value(0)                                             #else, turn the led OFF
        sleep_ms(200)                                            #stops the program for 0.2sec