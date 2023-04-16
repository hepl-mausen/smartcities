# Python functions used below

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

DHT(*pin*) : define used pin for the DHT11

redTempHumid() : read the temperature and humidity with DHT11

value() : fill the parentheses to set the pin value 

toggle() : switch the state of a pin



# DHT11 

![image](https://user-images.githubusercontent.com/124889423/232344415-d72a7bf7-5fa2-4fc2-8921-a24b328ddca8.png)

The DHT11 is a humidity and temperature sensor. 

## Display temperature and humidity on LCD 

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Temperature & Humidity Sensor
- Grove - 16 x 2 LCD

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232344735-4593f47f-0aaa-4d27-a578-f39f7aa2dcea.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232346874-a6623777-8f4f-4882-8ba0-e8ddc7af6f00.png)

### Demonstration : 

![341989659_889882195433516_634754055962956541_n](https://user-images.githubusercontent.com/124889423/232346900-915d4bcd-047a-4fd1-9616-c7e82f93ea37.jpg)


## Display temperature and humidity on LCD with alarm

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Temperature & Humidity Sensor
- Grove - 16 x 2 LCD
- Grove - Passive Buzzer

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232346972-cb5d6157-8506-45ce-9234-da046cc241cd.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232347081-82f49ef8-2751-43d3-9811-75b63e0c3645.png)

### Demonstration :

https://user-images.githubusercontent.com/124889423/232347167-c48448fa-c7bb-4fa6-aa98-51e5b8470836.mp4

# Mini fan 

To make the intelligent fan, we will use the Grove - Mini Fan, which consists of a motor drive board, DC motor, film blade and Grove connecting cables, as shown in the figure below. In general, motors can be divided into DC motors and AC motors according to the different input currents. Here, we use a DC motor. DC motors can realize the mutual conversion of electrical energy and mechanical energy so that electricity supplied to the motor can be used to drive other mechanical components.

![image](https://user-images.githubusercontent.com/124889423/232347599-fa91d6d5-49cc-4663-8470-4444b5f4fc9a.png)

A DC motor is composed of a stator and a rotor. The main function of the stator is to produce a magnetic field, and the main function of the rotor is to produce electromagnetic torque and induced electromotive force. In short, the DC motor works according to the principle that a conductor which carries an electrical current experiences a force in the magnetic field. Motors are widely used in our daily life, such as in industry, agriculture, and other applications where power is needed.

## Turning ON the fan while pressing the button

This code while turn on the fan while the button is pressed

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Mini Fan
- Grove - Button

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232347818-0ca5cd9f-4802-4ec6-9f61-2712d54d6f3b.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232347856-1ab7b32c-19b6-4e6d-af11-64f1cc99f82d.png)

### Demonstration :

https://user-images.githubusercontent.com/124889423/232347987-75e2bb44-8750-4204-8342-e94d06de6216.mp4


## Turning ON/OFF the fan while pressing the button

This code will change the state of the fan when the button is pressed

### Hardware needed :

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Mini Fan
- Grove - Button

### Connections : 

![image](https://user-images.githubusercontent.com/124889423/232348096-9e6cf870-b178-423b-8d7f-a0a7b07312aa.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232348105-56572e5d-2cd1-46ee-a4a4-23899733ce59.png)

# Demonstartions : 

https://user-images.githubusercontent.com/124889423/232348130-ce3c7822-4efb-42e8-b00c-bca558fcea92.mp4


## intellingent fan

This code make the fan "intellingent" by adding the temperature sensor and the LCD.

### Hardware needed : 

- Raspberry Pi Pico
- Grove Shield for Pi Pico
- Grove - Mini Fan
- Grove – Temperature & Humidity Sensor
- Grove - 16 x 2 LCD

### Connections :

![image](https://user-images.githubusercontent.com/124889423/232348211-13f6f6b6-064b-4086-a73c-bc161570c593.png)

### Code : 

![image](https://user-images.githubusercontent.com/124889423/232348375-0b1bbe5f-f0f1-4a63-9c09-e2ba5cad7a35.png)

### Demonstration : 


https://user-images.githubusercontent.com/124889423/232348698-a1f65799-ac1f-41c1-b19f-e6d3ed68925d.mp4

