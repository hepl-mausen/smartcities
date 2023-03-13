# Python functions used below

import ... : import a library.

Pin(*number, Pin.IN/OUT*) : define a pin number as an out/input by filling the parentheses.

For ... : start a for loop under conditions.

value() : put the value between parentheses on the selected Pin.

sleep_ms() : the program stops during the time set in the parentheses (in ms).

While ... : starting a while loop with a condition.


All the codes used below with comments : 

- [Button](Button.py)
- [BlinkingLed](BlinkingLed.py)

## Blink with for loop 

This code make a led blink with a for loop

### Hardware needed :

- Raspberry Pi Pico 
- Grove Shield for Pi Pico
- Grove - LED Pack

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/224554496-e7a73aaf-a442-4259-b2e4-17e7d6b2d574.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224554582-ea6712ea-4db8-4829-a1d5-6d502a1aab2c.png)

### Demonstartion : 

You can see the led blinking 10 times.

https://user-images.githubusercontent.com/124889423/224554670-5c156ccd-f622-4161-be91-171a1d759fb7.mp4



## Blink with while loop 

This code make a led blink with a while loop.

### Hardware needed : 

- Raspberry Pi Pico 
- Grove Shield for Pi Pico
- Grove - LED Pack

### Connections :

![image](https://user-images.githubusercontent.com/124889423/224554496-e7a73aaf-a442-4259-b2e4-17e7d6b2d574.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224554834-388e3665-0fef-4c9c-8691-e9aa50b8c452.png)

### Demonstration : 

You can see the led blinking.

https://user-images.githubusercontent.com/124889423/224555662-f0cea79f-e448-4f2a-bf98-2fa1c419aba7.mp4


## turning the led ON with the button

This code will turn the LED ON when the button is pressed

### Hardware needed : 

- Raspberry Pi Pico 
- Grove Shield for Pi Pico
- Grove - LED Pack
- Grove - Button

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/224555145-b1f8e41c-6669-4ab6-ac34-4cdc2017dc78.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224555189-96ddc008-4f8a-4ce1-8bf7-87e50ce46cb5.png)

### Demonstration : 

You can see the led turning ON when the button is pressed.

https://user-images.githubusercontent.com/124889423/224555244-70c66e0c-74db-47ce-b55b-36788add76ae.mp4



## switching led mode with the button

This code will switch the led state as the button is pressed.

### Hardware needed : 

- Raspberry Pi Pico 
- Grove Shield for Pi Pico
- Grove - LED Pack
- Grove - Button

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/224555145-b1f8e41c-6669-4ab6-ac34-4cdc2017dc78.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/224555477-44408286-886a-4eed-87cb-5d997f3fc48b.png)

### Demonstration : 

You can see that the led state switches as the button is pressed

https://user-images.githubusercontent.com/124889423/224555582-cb2d822e-3f55-49dc-b41f-6d02fb437a8d.mp4
