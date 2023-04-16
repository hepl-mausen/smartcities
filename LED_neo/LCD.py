#File : LCD
#Display some things on the LCD screen
#loic.mausen@student.hepl.be


#copy only the part you want to try


### Display 'hello world' on the LCD ###

from lcd1602 import LCD1602                                            #import functions from libraries 
from machine import I2C, Pin        
from utime import sleep_ms

i2c = I2C(1, scl=Pin(7), sda = Pin(6), freq = 400000)                  #define the pins for I2C

d = LCD1602(i2c, 2, 16)                                                #label data type, number of lines and characters per line 

d.display()                                                            #enable display                                                        

d.clear()                                                              #clear what's one the screen 
d.print('hello')                                                       #print 'hello' on the screen

d.setCursor(0, 1)                                                      #set display position, row and colum start from 0
d.print('world')                                                       #print 'hello' on the screen



### Print the rotary angle sensor value on the screen ###

from lcd1602 import LCD1602                                            #import functions from libraries 
from machine import I2C, Pin, ADC
from utime import sleep_ms

sensor =  ADC(0)                                                       #setting A0 as the ADC pin and naming it "sensor"

i2c = I2C(1, scl = Pin(7), sda = Pin(6), freq = 400000)                #define the pins for I2C
d = LCD1602(i2c, 2, 16)                                                #label data type, number of lines and characters per line 
d.display()                                                            #enable display

while True :                                                           #starting the while loop
    
    d.clear()                                                          #clear what's on the screen
    d.print(str(sensor.read_u16()))                                    #read the value the value of the sensor, turns it into a string and print it on tjhe screen
    sleep_ms(1000)                                                     #pause 1 sec
    
    
    
### Print the brightness value of the led  ###
    
from lcd1602 import LCD1602                                            #import functions from libraries
from machine import I2C, Pin, ADC, PWM
from utime import sleep_ms

sensor =  ADC(0)                                                       #setting A0 as the ADC pin and naming it "sensor"
led_pwm = PWM(Pin(18))                                                 #setting the pin 18 as an PWM output
led_pwm.freq(500)                                                      #setting the PWM frequence on 500
i2c = I2C(1, scl = Pin(7), sda = Pin(6), freq = 400000)                #define the pins for I2C
d = LCD1602(i2c, 2, 16)                                                #label data type, number of lines and characters per line
d.display()                                                            #enable display


while True :                                                           #starting the while loop 
    
    d.clear()                                                          #clear what's on the screen
    val = sensor.read_u16()                                            #read the value returned by the ADC and put it in val
    led_pwm.duty_u16(val)                                              #set the pwm duty cycle with val 
    d.print(str(val))                                                  #turn val into a string and print it on the screen
    sleep_ms(500)                                                      # pause for 0.5 sec
    

### Print the angle of the sensor on the LCD ###
    
    
from lcd1602 import LCD1602                                            #import functions from libraries
from machine import I2C, Pin, ADC, PWM
from utime import sleep_ms

sensor =  ADC(0)                                                       #setting A0 as the ADC pin and naming it "sensor"
i2c = I2C(1, scl = Pin(7), sda = Pin(6), freq = 400000)                #define the pins for I2C
d = LCD1602(i2c, 2, 16)                                                #label data type, number of lines and characters per line
d.display()                                                            #enable display


while True :                                                           #start the while loop
    
    d.clear()                                                          #clear what's on the screen
    val = sensor.read_u16()                                            #read the value returned by the ADC and put it in val
    val = round((val/65536)*360)                                       #turn the val value into degrees 
    d.print(str(val))                                                  #turn it into a string and print it on the screen
    d.write(0b11011111)                                                #print ° on the screen 
    sleep_ms(500)                                                      #pause for 0.5 sec 
