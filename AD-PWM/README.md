# Python functions used below

from ... import ... : import un function from a library.

ADC() : setting the pin between the parentheses as an ADC.

print() : print what's inside the parentheses in the console.

sleep() : the program stops during the time set in the parentheses (in sec).

sleep_ms() : the program stops during the time set in the parentheses (in ms).

Pin(*number, Pin.IN/OUT*) : define a pin number as an out/input by filling the parentheses. 

While ... : starting a while loop with a condition.

if ... : Startin a part of code under conditions.

read_u16() : read the value from the selected Pin on 16 bits (0 -> 65535).

value() : put the value between parentheses on the selected Pin.

PWM() : set the selected Pin as an PWM out/input.

freq() : set the PWM frequence by filling the parentheses.

duty_u16() : set the PWM duty cycle (16 bits) by filling the parentheses.

def *function* () : define a function to call later.

*function*() :  call the function previously created.






# Rotary Angle Sensor 

A rotary potentiometer is a device that can change its resistance value according to the rotation of the adjusting knob.

![image](https://user-images.githubusercontent.com/124889423/222922284-c89e0ae9-6b17-4952-8fdd-5dc14c489392.png)

When you rotate the knob, the sliding wiper connected to the knob slides on the resistive material with the rotation. With the sliding, the length of resistive material between A–B and B–C changes, which causes the resistance value and thus the output voltage to change accordingly. Using the Rotary Angle Sensor, we can easily input analog signals of different values to Pico.

You can find here all the programs tested below with comments : 

- [Rotary Angle Sensor](RotaryAngleSensor.py)
- [PWM](PWM.py)
- [Music](Music.py)




## Testing the sensor 

This program displays the analog value returned by the Rotary Angle Sensor in the Shell.

### Hardware needed :                   

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove Rotary Angle Sensor         

### Connections :

![image](https://user-images.githubusercontent.com/124889423/222924777-b985393d-ca51-4580-b392-2447907eddc6.png)

### Code :

![image](https://user-images.githubusercontent.com/124889423/224547382-1d65ae55-c886-4050-b6b0-75b2d0a81456.png)


### Demonstration :

You can see that the value returned by the ADC pin is changing over time as I turn the button. 

https://user-images.githubusercontent.com/124889423/224515877-a022cb25-c22f-42eb-ade9-4499120d72ee.mp4






## Turning the led on/off with the sensor

This program turn ON the led when the ADC pin value is under 30000.

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove LED Pack
- Grove Rotary Angle Sensor 

### Connections :

![image](https://user-images.githubusercontent.com/124889423/222927549-ccd5b85c-ab77-4f2b-97ca-2e8c23392474.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224547417-aa313516-bebe-4744-a771-9b2cfe436c1e.png)


### Demonstration : 

You can see that the led turns ON as the value returned by the ADC is under 30000.

https://user-images.githubusercontent.com/124889423/224545443-182a388a-c7f0-40d3-928b-2ede6be1a1d7.mp4









## Turning the led ON between 2 values

This program turn the LED ON when the ADC pin value is between 20000 an 45000

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove LED Pack
- Grove Rotary Angle Sensor 

### Connections :

![image](https://user-images.githubusercontent.com/124889423/222927549-ccd5b85c-ab77-4f2b-97ca-2e8c23392474.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224547449-0f7c7b2e-fa39-4b71-ab90-83e6df4f8ef2.png)

### Demonstration : 

You can see that the led turns ON as the value returned by the ADC is between 20000 and 45000.

https://user-images.githubusercontent.com/124889423/224545824-b02ef391-2af1-499e-b3a6-5a1ddcdd6184.




# PWM with python

PWM is short for pulse width modulation. Where, “pulse" refers to the pulse signal, which is a digital signal sent out at periodic continuous on and off patterns by the microcontroller. Because the signal sent out by the transistor only has two states, on and off, the signal switches only between high level and low level. PWM pulse signal is mainly defined by three components: cycle, duty cycle and frequency.

As shown in the figure below, cycle (T) is the total time for a pulse signal to go through a high-level state (T1) and a low-level state (T2), that is, cycle (T) = T1 + T2. Duty cycle represents the ratio of the time when the signal is at a high level to the cycle in a cycle, so a duty cycle can be calculated as cycle T1 / T. It can be expressed in percents. 

![image](https://user-images.githubusercontent.com/124889423/224546678-11d0024f-48e7-40aa-a58c-607be6a5a26e.png)




## Brightness of the led with the rotary angle sensor

This program modify the brightness of the led based on the value returned by the ADC pin. 

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove LED Pack
- Grove Rotary Angle Sensor 

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/224547242-e95eba42-70fe-4dc9-96c4-b57835cec949.png)

### Code : 
 
 You can see that the led brightness is modified as I turn the potentiometre.
 
![image](https://user-images.githubusercontent.com/124889423/224547332-0c272407-d768-4d32-8f02-4fddb4651da4.png)

### Demonstration : 

You can see the brightness of the led beeing modified as I turn the potentiometre.

https://user-images.githubusercontent.com/124889423/224548846-790e5fe6-2b2d-405f-a3e3-6a4ec34a329e.mp4



## Brightness from dark to light then from light to dark

The code make the LED go from dark to light then from light to dark. 

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove LED Pack

### Connections :

![image](https://user-images.githubusercontent.com/124889423/224548140-7d3c1507-1793-4985-b314-0c3b00db412d.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224548241-4d354d49-7c7d-4577-b06c-6dfe36159a67.png)

### Demonstration : 

You can see the brightness of the led beeing modified automatically.

https://user-images.githubusercontent.com/124889423/224548573-563c2971-e1bc-43c5-b655-585419fc796c.mp4






## Making The Imperial March - STAR WARS with the buzzer 

This code make the Imperial March from STAR WARS with the buzzer.

### hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Passive Buzzer

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/224550337-1eabdb12-7f2d-4e15-a256-42448a2e3a98.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224550502-a547939b-b1f1-4274-bdc3-379f9942c97f.png)
![image](https://user-images.githubusercontent.com/124889423/224550570-0fe73a11-1891-41d1-a177-af639f75c3ba.png)
![image](https://user-images.githubusercontent.com/124889423/224550617-ae5e96bb-d1fc-4b15-a43c-ccf8d59a49f6.png)
![image](https://user-images.githubusercontent.com/124889423/224550636-b0bafbc9-a687-4356-a51a-43f0298c706a.png)
![image](https://user-images.githubusercontent.com/124889423/224550656-3565db9c-7b21-4def-840e-52bb8db54b8e.png)

### Demonstration : 

You can hear the Imperial March from STAR WARS ! 

https://user-images.githubusercontent.com/124889423/224550912-03ec879f-9e98-498b-a7d0-8110ee54bdef.mp4
