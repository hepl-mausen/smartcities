#File : Light
#Making an intelligent light 
#loic.mausen@student.hepl.be

#copy only the part you want to try



### switching colors of the led

from ws2812 import WS2812               #import functions from library 
from utime import sleep_ms

black = (0,0,0)                         #set color parameters
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)
COLORS = (black, red, yellow, green, cyan, blue, purple, white)

led = WS2812(18,1)                      #set led pins and define the led count

while True:                             #starting a while loop 
    print("fills")                      #print fills in the consol 
    for color in COLORS:                #start a for loop, for every color of the list COLORS
        led.pixels_fill(color)          #set the color of the led 
        led.pixels_show()               #display the color 
        sleep_ms(200)                   #wait 200 ms


        
### intellingent light ###
        
from ws2812 import WS2812               #import functions from library 
from utime import sleep_ms
from machine import I2C, Pin, ADC

led = WS2812(18,1)                      #set led pins and define the led count
lightsensor = ADC(0)                    #define light sensor pins 
soundsensor = ADC(1)                    #define sound sesnor pins 

while True:
    light = lightsensor.read_u16()/256          #read the light sensor value on 16 bits and divide it by 256
    average = 0                                 #set the value of average on 0
    for i in range (1000):                      #start a for loop
        noise = soundsensor.read_u16()/256      #read the sound value on 1§ bits and divide it by 256
        average += noise                        #add the noise value 1000 times
    noise = average/1000                        #make an average of the values
    
    print(noise)                                #print 'noise' in the consol 
    if light < 80:                              #if the value of 'light' is under 80
        led.pixels_fill((255,255,255))          #set the color of the led on white 
        led.pixels_show()                       #display the color 
        sleep_ms(200)                           #wait 200 ms
    else:
        if noise < 25:                          #if noise is under 25 
            led.pixels_fill((0,255,0))          #set the color on green 
            led.pixels_show()                   #display color 
            sleep_ms(1000)                      #wait 1000 ms
        if noise >= 25 and noise < 50:          #if the value of noise is between 25 and 50
            led.pixels_fill((255,255,0))        #set the color on orange
            led.pixels_show()                   #display the color 
            sleep_ms(1000)                      #wait 1000 ms
        if noise >= 50:                         # if noise is above 50
            led.pixels_fill((255,0,0))          #set the color on red 
            led.pixels_show()                   #display the color 
            sleep_ms(1000)                      #wait 1000 ms



### rainbow with light ###

from ws2812 import WS2812                       #import libraries
from utime import sleep_ms

led = WS2812(18,1)                             #set led pins and define the led count

while True:    
    led.rainbow_cycle(0)                        #make the led colors change to take all the values
    
    
### other way to do it ###
    
from ws2812 import WS2812                       #import libraries           
from utime import sleep_ms

black = (0,0,0)                                 #set colors parameters
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)
COLORS = (black, red, yellow, green, cyan, blue, purple, white)      #make a list with the colors 

led = WS2812(18,1)                             #set led pins and define the led count

while True:                                    #start a while loop
    for color in COLORS:                       #start a for loop, for every color of the list
        led.pixels_fill(color)                 #set the color on of the led 
        led.pixels_show()                      #display color
        sleep_ms(200)                          #wait 200 ms


### other way to do it ###

from ws2812 import WS2812                      #import libraries
from utime import sleep_ms

black = (0,0,0)                                #set colors parameters
red = (255,0,0)
yellow = (255,150,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
purple = (180,0,255)
white = (255,255,255)
COLORS = (black, red, yellow, green, cyan, blue, purple, white)                #make a list with the colors 

led = WS2812(18,1)                                   #set led pins and define the led count



while True:                                           #start while loop 
    for color in COLORS:                              #start a for loop, for every 
        led.color_chase(color, 0.01)                  #display every color 1 by 1 with 0.01 sec of delay 