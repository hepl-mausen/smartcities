# Rotary Angle Sensor 

A rotary potentiometer is a device that can change its resistance value according to the rotation of the adjusting knob.

![image](https://user-images.githubusercontent.com/124889423/222922284-c89e0ae9-6b17-4952-8fdd-5dc14c489392.png)

When you rotate the knob, the sliding wiper connected to the knob slides on the resistive material with the rotation. With the sliding, the length of resistive material between A–B and B–C changes, which causes the resistance value and thus the output voltage to change accordingly. Using the Rotary Angle Sensor, we can easily input analog signals of different values to Pico.

You can find [here](RotaryAngleSensor.py) all the programs tested below with comments.


## Testing the sensor 

This program displays the analog value returned by the Rotary Angle Sensor in the Shell.

### Hardware needed :                   

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove Rotary Angle Sensor         

### Connections :

![image](https://user-images.githubusercontent.com/124889423/222924777-b985393d-ca51-4580-b392-2447907eddc6.png)

### Code :

![image](https://user-images.githubusercontent.com/124889423/222926257-13a0c216-ac67-4e5d-b1b7-8381b8482426.png)

### Demonstration :

You can see that the value returned by the ADC pin is changing over time as I turn the button. 

![image](https://user-images.githubusercontent.com/124889423/222926666-7c6f0ef9-7e4d-47a1-ad1a-03980d62feb6.png)



## Turning the led on/off with the sensor

This program turn ON the led when the ADC pin value is up 30000.

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove LED Pack
- Grove Rotary Angle Sensor 

### Connections :

![image](https://user-images.githubusercontent.com/124889423/222927549-ccd5b85c-ab77-4f2b-97ca-2e8c23392474.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/222927698-163d48fe-a7cf-4a1b-8931-917607508984.png)

### Demonstration : 

https://user-images.githubusercontent.com/124889423/222928360-0e53c263-0f29-4865-8ba2-8ac405d8bbd3.mp4

You can see that the LED turn off as I turn the knodn. (When the value returned by the ADC pin goes up 30000)




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

![image](https://user-images.githubusercontent.com/124889423/222929980-a1574a82-1b4b-43c2-8f16-dd6510a4eaf6.png)


### Demonstration : 

https://user-images.githubusercontent.com/124889423/222930946-374efc23-23f6-4ba6-8e30-b8ced1f53988.mp4

You can see that the LED turn ON a quick moment. It turns ON when the returned ADC pin value is between 20000 and 45000. 
