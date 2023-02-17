# smartcities
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

