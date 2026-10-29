## GIMX-evdev

### Linux Build Instructions

I will work on modernizing Linux build instructions and installation support over time as I plug away on this project.

Here is a link to the document I am maintaining, mostly copied from matlo, but his site doesn't directly apply to this build in all ways and might not always be around, so it's worth maintaining documentation here separately.

[[Linux Build Instructions]

GIMX is a free software that allows to use a computer as a hub for your gaming devices. It works on Windows® and GNU/Linux platforms. It is compatible with Playstation® and Xbox® gaming consoles. The connection between the computer and the gaming console is performed using a USB adapter – [get one on the GIMX shop!](https://blog.gimx.fr/product/gimx-adapter/) – or a Bluetooth® dongle (PS3/PS4 only). The capabilities depend on the platform, the connection method, and the gaming platform.

GIMX on Linux now has evdev support, which is more supported on modern Linux kernels.  

This is a fork of GIMX for Linux systems where evdev support has resulted in joydev neglect and degraded functionality.  

If you find you're using GIMX by matlo on a certain non-ubuntu distro and it just refuses to do something like, accept proper analog joystick or throttle inputs, it might be a critical kernel level difference in expected behaviour and your best bet is to either swithc to the OS distro he built the software on, or try out evdev.  

### Nintendo Switch Support

Based on https://github.com/hisptoot/GIMX/tree/master

I have pulled diffs from Hisptoot to generate their firmware for the ATmega32U4 Arduino microcontroller in the GIMX cable, and after finding some issues with stability, I have adapted the behaviors after several rounds of diagnostics and testing, to produce a more stable Nintendo Switch based firmware, to allow spoofing a Nintendo Switch Pro controller.  This does not have motion control support at this time, but it works well with basic controls so far.  Part of my work with this project is to expand the support of GIMX with more stable console support for consoles I own and can test on.

TODO:

* Hardening NSW firmware against rare and unlikely, but possible failure conditions.  Firmware appears stable but could use better handling for interrupt protection, reset recovery, packet parsing, and review potentially unbounded USB waits.
* Adding support to WAKE the Nintendo Switch - while in sleep mode docked in the console, with a GIMX cable connected to the switch, it is incapable of waking the Switch the way real controllers can.
* Potentially, adding bluetooth controller support with bluetooth spoofing the way it is supported for PS3 and PS4 by spoofing the BT MAC and protocols of a paired Switch Pro controller.  This is lower priority and I don't think I'm likely to do this but we'll see.

**WARNING** this version is not officially supported by matlo, and while you can download all the configs from their repository, they will NOT work!  This is because evdev ID numbers are different and names of devices might be fetched differently.  You won't be able to match any old configs.  But you CAN still download them and use them as references for remapping, as many of them have nice advanced features and offer structure to work from.

Please report any bugs with identifying your devices, and send your device and device ID found with `evdev-test` or `cat /proc/bus/input/devices`

Links:
* [Documentation](https://wiki.gimx.fr)  
* [Source code](https://gimx.fr/source)  
* [Issue tracker](https://gimx.fr/buglist)  
* Licence: [GPLv3](https://www.gnu.org/copyleft/gpl.html)  
* [Donations](https://blog.gimx.fr/give/gimx-donations-current/)
