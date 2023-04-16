# Python functions used below 

from ... import ... : import un function from a library.

ADC() : setting the pin between the parentheses as an ADC.

print() : print what's inside the parentheses in the console.

sleep_ms() : the program stops during the time set in the parentheses (in ms).

Pin(*number, Pin.IN/OUT*) : define a pin number as an out/input by filling the parentheses. 

While ... : starting a while loop with a condition.

read_u16() : read the value from the selected Pin on 16 bits (0 -> 65535).

for ... : start a loop that lasts a certain time

pixels_fill() : set the color you want display between the parentheses

pixels_show() : turn the led on and display the previous set color

WS2812(*pin number,led count*) : define the pin used and the led count

rainbow_cycle(*number of cycle*) : display every color on the led during x cycles

color_chase(*color, time between colors*) : change the color displayed by the led every x seconde



# RGB Led

We will use the ws2813 mini. 

![image](https://user-images.githubusercontent.com/124889423/232336646-210cec74-4558-461d-b50a-39196d946d4d.png)

When we set RGB LED to display different colors, we only need to set the values of red (R), green (g), and blue (b) respectively. The red, green and blue color channels are divided into 256 levels of brightness, that is, 0-255. The value of 0 is the least bright, which is synonymous with turning off the light, while the most bright at the value of 255.

Colors and how the create them : 

![image](https://user-images.githubusercontent.com/124889423/232336908-a4f75890-6efd-4380-8216-ca12e8ed9db0.png)


## Switching the colors of the led 
This code will mak a the led change of colors with a list and a for loop.
### hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - RGB LED (WS2813 Mini)

### Connections :
![image](https://user-images.githubusercontent.com/124889423/232337614-512d64f9-f215-4844-9539-17a6dc3b89a6.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232337649-12fc0fb8-1170-4175-9da7-44ef59cd1237.png)

### Demonstration :

https://user-images.githubusercontent.com/124889423/232337826-351aaa16-650d-4916-b0bd-1c4934c17be1.mp4


## intellingent light

This code make the led change of colors with a list under certain conditions 

### Hardware needed :
- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - RGB LED (WS2813 Mini)
- Grove - Light Sensor
- Grove - Sound Sensor

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232340993-8a736cf3-6979-4d14-82bf-ca17f7573687.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232341138-4b68ad65-870a-455a-b41e-b4d914e572e9.png)

### Demonstration : 

https://user-images.githubusercontent.com/124889423/232341584-6a88517f-71fc-4353-be16-c5531ae1c36f.mp4


## 3 ways to make a rainbow

### Hardware needed :
- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - RGB LED (WS2813 Mini)

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232337614-512d64f9-f215-4844-9539-17a6dc3b89a6.png)

### Code using rainbow function : 

![image](https://user-images.githubusercontent.com/124889423/232342620-5c27097a-2b9b-44e6-b348-93e164d05a39.png)

### Demonstration : 

https://user-images.githubusercontent.com/124889423/232342634-48402c9b-7d8c-4beb-85f4-7e66ed4a0556.mp4

### Code using chase function : 

![image](https://user-images.githubusercontent.com/124889423/232342659-9201b05d-2894-47a4-919a-c69a95b45c90.png)

### Demonstration : 

https://user-images.githubusercontent.com/124889423/232343051-84abf9fb-bcb4-4185-8444-e29747e962a6.mp4

### Code using the previous functions 

![image](https://user-images.githubusercontent.com/124889423/232343224-0dbb3fa5-6de2-44c7-8e25-b3a0172af134.png)

### Demonstration 

https://user-images.githubusercontent.com/124889423/232343229-0c94be14-c10f-4839-91a3-767ac6f4f757.mp4
