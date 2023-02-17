# LED

Codes to make a LED turn on/off 

## Turning the LED on

 import machine
 
 LED = machine.Pin(16,machine.Pin.OUT)

 LED.value(1)
 
 ## Turning the LED off
 
 import machine
 
 LED = machine.Pin(16,machine.Pin.OUT)

 LED.value(0)
 
 ## Making the LED blink with a for loop 
 
import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)
 
for i in range (10):

    LED.value(1)
    
    utime.sleep_ms(1000)
    
    LED.value(0)
    
    utime.sleep_ms(1000)
