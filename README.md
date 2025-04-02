# camera-pizero
Raspberry Pi Zero and Raspberry Pi Camera Module based camera

## Components
* Raspberry Pi Zero
* Raspberry Pi Camera Module
* Extendded camera ribbon for pi zero
* 3.5in LCD SPI Raspberry Pi Screen
* 7mm push button
* 2-pin female housing connector
* Mini Slide Switch 2-Position SPDT
* [AA Makeshift Battery Holder 3](https://makerworld.com/en/models/452852-aa-makeshift-battery-holder-1-2-3-4-6-8-10-12#profileId-360121)
* 3xAA Batteries
* Micro-USB cable
* 2x M2.5 4mm screws
* 4x M2.5 6mm screws
* 4x M2 6mm screws
* 4x M2 10mm screws
* 6x M2.5 nuts
* 8x M2 nuts

## Assembly instructions
* Wire the push button to the 2-pin female housing connector.
* Wire the Battery Holder and Slide Switch and the micro usb cable by cutting off the USB-A connector.
* Connect the camera module to the raspberry pi through the cable hole.
* Assemble the camera module with the hood on the case.
* Assemble the raspberry pi on the case.
* Assemble the Slide Switch to the case.
* Assemble the Push Button on the case,
* Assemble the Battery Holder to the case with screw heads on the inside.
* Connect the push button connector to the pins 33/34 of the raspberry pi.
* Connect the micro-usb connector to the power connector (right) of the raspberry pi.
* Connect the screen to the raspberry pi.
* Assemble the cover to case using a length of spare print filament.
* Insert memory card if not done prior to assembly.
* Insert batteries.

Note: During the software installation better use a usb power supply.


## Software
Prequesistes
* Raspberry Pi OS Lite bookworm

Copy the repository in the Raspberry pi and run the install script
```
cd src/
sudo bash install.sh
```