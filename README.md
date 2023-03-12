# Raspberry Pi Pico W
## The Raspberry Pi Pico family

The Raspberry Pi Pico W belongs to the Raspberry Pi Pico family (4 boards). Key features of those boards : 

- [RP2040](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040) microcontroller chip

- [Dual-core Arm Cortex M0+ processor](https://www.st.com/content/st_com/en/arm-32-bit-microcontrollers/arm-cortex-m0-plus.html), flexible clock running up to 133 MHz

- 264kB of SRAM, and 2MB of on-board flash memory

- USB 1.1 with device and host support

- Low-power sleep and dormant modes

- Drag-and-drop programming using mass storage over USB

- 26 × multi-function GPIO pins

- 2 × SPI, 2 × I2C, 2 × UART, 3 × 12-bit ADC, 16 × controllable PWM channels

- Accurate clock and timer on-chip

- Temperature sensor

- Accelerated floating-point libraries on-chip

- 8 × Programmable I/O (PIO) state machines for custom peripheral support

## Raspberry Pi Pico W

Raspberry Pi Pico W adds on-board single-band 2.4GHz wireless interfaces ([802.11n](https://www.electronics-notes.com/articles/connectivity/wifi-ieee-802-11/802-11n.php)) using the [Infineon CYW43439](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/) while retaining the Pico form factor. The on-board 2.4GHz wireless interface has the following features:

- Wireless ([802.11n](https://www.electronics-notes.com/articles/connectivity/wifi-ieee-802-11/802-11n.php)), single-band (2.4 GHz)

- [WPA3](https://www.okta.com/identity-101/wpa3-security/)

- Soft access point supporting up to four clients

The antenna is an onboard antenna licensed from ABRACON (formerly ProAnt). The wireless interface is connected via [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to the [RP2040](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040) microcontroller.

Due to pin limitations, some of the wireless interface pins are shared. The CLK(clock) is shared with VSYS(main system input voltage) monitor, so only when there isn’t an [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) transaction in progress can VSYS be read via the ADC. The [Infineon CYW43439](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/wi-fi-4-802.11n/cyw43439/) DIN/DOUT and [IRQ](https://www.computerhope.com/jargon/i/irq.htm) all share one pin on the [RP2040](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#welcome-to-rp2040). Only when an [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) transaction isn’t in progress is it suitable to check for [IRQ](https://www.computerhope.com/jargon/i/irq.htm)s. The interface typically runs at 33MHz.

For best wireless performance, the antenna should be in free space. For instance, putting metal under or close by the antenna can reduce its performance both in terms of gain and bandwidth. Adding grounded metal to the sides of the antenna can improve the antenna’s bandwidth.

## Raspberry Pi Pico W pinout

![image](https://user-images.githubusercontent.com/124889423/219525153-2640afc4-45bf-42d0-8334-2d62fdc0fd4f.png)

# MicroPython

MicroPython is a full Python compiler and runtime that runs on the bare-metal. You get an interactive prompt (the REPL) to execute commands immediately, along with the ability to run and import scripts from the built-in filesystem. The REPL has history, tab completion, auto-indent and paste mode for a great user experience.

MicroPython strives to be as compatible as possible with normal Python (known as CPython) so that if you know Python you already know MicroPython. On the other hand, the more you learn about MicroPython the better you become at Python.

In addition to implementing a selection of core Python libraries, MicroPython includes modules such as "machine" for accessing low-level hardware.


# Grove Kit

## Grove  Shield

The Grove Shield for Pi Pico v1.0 is a plug-and-play shield for Raspberry Pi Pico which integrates with various kinds of Grove connectors, such as I2C, UART, Digital, Analog ports. It enables you to build prototypes and projects in an easy and quick way without soldering or jumper wires

### Features : 

- **Grove & GPIO Expansion Board for Pico** : Break out all the pins and power of the Raspberry Pi Pico to provide full female headers and 10 additional Grove ports.
- **Rich Peripherals for Grove** : Provide 10 Grove ports including 2x I2C, 2x UART, 3x Digital, and 3x Analog, which also contains 1x SPI port, 1x power switch, and the SWD Debug interface.
- **Plug and Play**: Benefit convenient Grove connectors that supports multiple Grove components.
- **Platform Support**: MicroPython & Arduino.

This is the perfect expansion board for Raspberry Pi Pico represented by Seeed Studio, where it breaks out all the pins and power of the board to produce additional Grove ports and led out full female headers, SWD debug interface, SPI pin. With its convenient feature and Grove system supported, it will be your good assistant that helps you quickly develop your projects.

The Grove connector on the board includes 2x I2C, 2x UART communication ports, and 3*Analog with 3*Digital transmitted ports. The internal of the two female headers are directly attached to a Raspberry Pi Pico and the external two are for standard Raspberry Pi Pico pins. You can directly use Pre-Soldered Pico and plug it into the shield board. Additionally, there is an SWD debug interface, the SPI pin, and one 5V/3.5V changeable switch, for your further usage.

## The Kit 

This is a Grove starter kit designed for Raspberry Pi Pico. It includes 5 sensors/ 5 actuators/ 2LEDs/ 1 LCD display/ 1 Grove shield, it will help you get started with Raspberry Pi Pico quickly and comprehensively.

### Key features

- Get Started with Raspberry Pi Pico easily and quickly 
- 14 handpicked Grove Modules, including 5 sensors/ 5 actuators/ 2LED/ 1 LCD display/ 1 Grove shield  
- Detailed and comprehensive Micropython tutorials for each module  (Arduino Guide is on the way) 
- No wiring, no welding, plug & play experience

### Description 

Raspberry Pi Pico swept the MCU world like a huge wave. Pico born with powerful performance, reasonable price, and comprehensive resources, it will definitely become a great platform for learning and mastering electronic knowledge.  

To help you ride this wave, we launched the Grove Starter Kit for Raspberry Pi Pico as soon as possible. We have selected the most common sensors, actuators, and displays in this kit. With the help of the Grove Pico shield, you can connect all these modules to the Pico simply by plugging and unplugging. This will greatly reduce the difficulty to use Raspberry Pi Pico for learning and project prototyping, and help you quickly get started with Micropython. 

In the meantime, we provide detailed tutorials for each module. Micropython is currently supported, and Arduino is expected to be supported soon. This means with this kit, you can choose a programming language that suits you to quickly turn on an LED light, control a motor, servo, read the values of various sensors, and display them on the LCD display.

### Part List

- Grove - LED Pack	*1
- Grove - RGB LED (WS2813 Mini)	*1
- Grove - Light Sensor	*1
- Grove - Sound Sensor	*1
- Grove - Rotary Angle Sensor	*1
- Grove - Temperature & Humidity Sensor	*1
- Grove - mini PIR motion sensor	*1
- Grove - Passive Buzzer	*1
- Grove - Button	*1
- Grove - Servo	*1
- Grove - Mini Fan 	*1
- Grove - Relay	*1
- Grove - 16x2 LCD	*1
- Grove Shield for Pi Pico 	*1
- Grove Cable	*8

# Thonny 
Thonny is a Python IDE for begginers

## Features : 

**Easy to get started**. Thonny comes with Python 3.10 built in, so just one simple installer is needed and you're ready to learn programming. (You can also use a separate Python installation, if necessary.) The initial user interface is stripped of all features that may distract beginners.   

![image](https://user-images.githubusercontent.com/124889423/224557222-228af6e3-db79-49ee-8ef7-3f789ff7c8d1.png)


**No-hassle variables**. Once you're done with hello-worlds, select View → Variables and see how your programs and shell commands affect Python variables.

![image](https://user-images.githubusercontent.com/124889423/224557299-9033be6a-5226-4b2b-9fc5-8d224e898164.png)

**Simple debugger**. Just press Ctrl+F5 instead of F5 and you can run your programs step-by-step, no breakpoints needed. Press F6 for a big step and F7 for a small step. Steps follow program structure, not just code lines.

![image](https://user-images.githubusercontent.com/124889423/224557377-cd908158-dc00-4c49-a209-8b3f8e28eed0.png)

**Step through expression evaluation**. If you use small steps, then you can even see how Python evaluates your expressions. You can think of this light-blue box as a piece of paper where Python replaces subexpressions with their values, piece-by-piece.

![image](https://user-images.githubusercontent.com/124889423/224557411-a3a1780c-482b-42e1-be25-e02efe7741cd.png)

**Faithful representation of function calls**. Stepping into a function call opens a new window with separate local variables table and code pointer. Good understanding of how function calls work is especially important for understanding recursion.

![image](https://user-images.githubusercontent.com/124889423/224557443-914b9722-2a12-4a1d-a2ad-360f21678c30.png)

**Highlights syntax errors**. Unclosed quotes and parentheses are the most common beginners' syntax errors. Thonny's editor makes these easy to spot.

![image](https://user-images.githubusercontent.com/124889423/224557464-810f8b9c-01a9-4440-af28-8216243bf958.png)

**Explains scopes**. Highlighting variable occurrences reminds you that the same name doesn't always mean the same variable and helps spotting typos. Local variables are visually distinguished from globals.

![image](https://user-images.githubusercontent.com/124889423/224557485-25eb5d57-8445-45e6-b62f-49a643626512.png)

**Mode for explaining references**. Variables are initially presented according to simplified model (name → value) but you can switch to more realistic model (name → address/id → value).

![image](https://user-images.githubusercontent.com/124889423/224557496-c60bcc35-20c6-450c-bab0-542932fc9ed1.png)

**Code completion**. Students can explore APIs with the help of code completion.

![image](https://user-images.githubusercontent.com/124889423/224557529-0b8c81b0-0516-44f6-9988-c22ba642c680.png)

**Beginner friendly system shell**. Select Tools → Open system shell to install extra packages or learn handling Python on command line. PATH and conflicts with other Python interpreters are taken care of by Thonny.

![image](https://user-images.githubusercontent.com/124889423/224557560-5f321cce-089d-468c-b9b5-a917bbdbccca.png)

**Simple and clean pip GUI**. Select Tools → Manage packages for even easier installation of 3rd party packages.

![image](https://user-images.githubusercontent.com/124889423/224557578-d82df03e-a7ec-4002-b98b-6fd9125732e7.png)
