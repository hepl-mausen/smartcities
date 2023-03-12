#File : PWM
#using PWM with rpi pico
#loic.mausen@student.hepl.be

#copy only the part you want to try


### Brightness of the led with the rotary angle sensor ###

from machine import Pin, PWM, ADC                           #import functions from libraries

led_pwm = PWM(Pin(18, Pin.OUT))                             #setting the pin 18 as an PWM output an naming it led_pwm
sensor = ADC(0)                                             #setting A0 as the ADC pin and naming it "sensor"

led_pwm.freq(500)                                           #setting the pwm frequency to 500

while True:                                                 #starting the while loop
    led_pwm.duty_u16(sensor.read_u16())                     #using the value of the ADC pin (16bits) to set the duty cycle value (16bits)


    
### Brightness from dark to light then from light to dark ###
    
from machine import Pin, PWM                                #import functions from libraries 
from utime import sleep_ms

led_pwm = PWM(Pin(18, Pin.OUT))                             #setting the pin 18 as an PWM output an naming it led_pwm
val = 0                                                     #setting the value of val on 0

led_pwm.freq(500)                                           #setting the pwm frequency to 500

while True:                                                 #starting the while loop

    while val < 65535:                                      #while val is under 65535
        val = val + 50                                      #increment val by 50
        led_pwm.duty_u16(val)                               #setting the value of the duty cycle (16 bits) to val
        sleep_ms(1)                                         #stops the program for 1 sec
        
    while val > 0:                                          #while val is above 0
        val = val - 50                                      #decrement val by 50
        led_pwm.duty_u16(val)                               #setting the value of the duty cycle (16 bits) to val 
        sleep_ms(1)                                         #stops the program for 1 sec
        

