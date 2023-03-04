#File : RotaryAngleSensor
#testing the rotary angle sensor
#loic.mausen@student.hepl.be

#uncomment the part you want to try



### testing the sensor ###

# from machine import ADC
# from utime import sleep
# 
# angle = ADC(0)
# 
# while True:
#     print(angle.read_u16())
#     sleep(1)
    
    
    
### Turning the led on/off with the sensor ###

# from machine import ADC, Pin
# from time import sleep_ms
# 
# led = Pin(16, Pin.OUT)
# sensor = ADC(1)
# 
# while True:
#     print(sensor.read_u16())
#     if sensor.read_u16() < 30000:
#         led.value(1)
#         sleep_ms(200)
#     else:
#         led.value(0)
#         sleep_ms(200)
        
        
        
### Turning the led ON between 2 values ###

# from machine import ADC, Pin
# from time import sleep_ms
# 
# led = Pin(16, Pin.OUT)
# sensor = ADC(1)
# 
# while True:
#     print(sensor.read_u16())
#     if sensor.read_u16() > 20000 and sensor.read_u16() < 45000:
#         led.value(1)
#         sleep_ms(200)
#     else:
#         led.value(0)
#         sleep_ms(200)