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

We will use the ws2813 mini. When we set RGB LED to display different colors, we only need to set the values of red (R),
green (g), and blue (b) respectively. The red, green and blue color channels are divided into 256
levels of brightness, that is, 0-255. The value of 0 is the least bright, which is synonymous with
turning off the light, while the most bright at the value of 255.
