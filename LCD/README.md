# Python fucntions used below 

from ... import ... : import un function from a library.

ADC() : setting the pin between the parentheses as an ADC.

print() : print what's inside the parentheses in the console.

sleep_ms() : the program stops during the time set in the parentheses (in ms).

Pin(*number, Pin.IN/OUT*) : define a pin number as an out/input by filling the parentheses. 

While ... : starting a while loop with a condition.

read_u16() : read the value from the selected Pin on 16 bits (0 -> 65535).

PWM() : set the selected Pin as an PWM out/input.

freq() : set the PWM frequence by filling the parentheses.

duty_u16() : set the PWM duty cycle (16 bits) by filling the parentheses.

I2C(*I2C peripheral*, *scl pin*, *sda pin*, *maximum frequence of the scl*) : define the pins for I2C

LCD1602(*label data type*, *number of lines*, *number of characters per line*) : function of the lcd1602 library to print on the screen 

display() : enable display on the screen 

setCursor(*row*, *column*) : set display position

str() : turn what's into the parentheses in a string

write() : used to write specific things on the LCD


# LCD

LCD (for *liquid-crystal display*) are screens based on the changing refractive index of the liquid inside of it when affected by an electric field. 
When affected by specific electric fields, the molecules of the liquide will turn in different directions, thus changing the refractive index of the liquid crystal, and affecting the direction of passing light.
Therefore, the final imaging effect of LCD can be determined as long as the undesired light is filtered out through a polarizer.

![image](https://user-images.githubusercontent.com/124889423/226195798-6368cff5-425f-4dc5-acce-e781c415ef97.png)

Significantly, the liquid crystal itself cannot produce light, it can only change the direction of the light passing through it. So, in addition to the liquid crystal layer, we often need a backlight panel as the light source in an LCD.

You can find here all the programs tested below with comments, save [this code](lcd1602.py) in the RPi Pico to make it work :

- [LCD](LCD.py)


This program displays 'Hello world' on the screen

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - 16 x 2 LCD

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/226197269-13a6df59-fdbb-4ae8-824b-fc3ec7ba02f4.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/226199130-e07cd512-65a8-49a7-b3f4-b1a19c07a5d7.png)

### Demonstration :

![image](https://user-images.githubusercontent.com/124889423/226199159-93d7d99a-ffad-4617-88a2-dbd2f9e6b936.png)




## Print the rotary angle sensor value on the screen 

This code will display the value returned by the ADC on the screen. 

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - 16 x 2 LCD
- Grove - Rotary Angle Sensor

### Connections :

![image](https://user-images.githubusercontent.com/124889423/226201012-d76a65a9-8e57-4bf7-a881-ef47aca56228.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/226201080-3a4732cd-bb8d-486b-8b02-490c1a9e679e.png)

### Demonstration :

https://user-images.githubusercontent.com/124889423/226201380-a8308d2d-ad82-40cb-82ad-999941812707.mp4




## Print the brightness value of the led

This code adjust the value of the led based on the value of the ADC and print it on the screen.

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - 16 x 2 LCD
- Grove - Rotary Angle Sensor
- Grove - LED Pack

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/226203274-485733e4-68b6-4873-918b-3ec634e0f718.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/226203304-8bcdfdda-dd04-4bad-a7cd-c5cd4c648b41.png)

### Demonstration : 

![image](https://user-images.githubusercontent.com/124889423/226203354-0cf6aeed-03af-460b-ac64-ea1289d147e3.png)




## Print the angle of the sensor on the LCD : 

This code print the angle of the potentiometre in °. It can not reach 0° because there is always a current in the potentiometre. (see [AD-PWM](AD-PWM) to understand how the potentiometre works)

### Hardware needed :

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - 16 x 2 LCD
- Grove - Rotary Angle Sensor

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/226204155-701d31e4-944b-4ba9-a80a-b1866006c5aa.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/226204193-cbcf69fe-3dee-4719-9f1e-029986d7c65d.png)

### Demonstration : 

https://user-images.githubusercontent.com/124889423/226204378-3696fd4e-aa89-48d5-81b4-6ffed444218e.mp4
