# Controlling a Thymio robot from the Raspberry Pi

Download [ https://www.thymio.org/en:linuxinstall]

This will install a new Raspberry menu item
* Education
 * Aseba Challenge
 * Aseba Online Help
 * Aseba Playground
 * Aseba Studio
 * Aseba Studio for Thymio
 * Thymio Firmware Upgrader (upgrade to version 11)
 * Thymio VPL (Visual Programming Language)
 * Thmyio Network Configurator

https://www.thymio.org/en:thymioraspyexample

```
sudo pip3 install --upgrade pip
sudo pip3 install pydbus

/home/pi/.virtualenvs/py3cv3/bin/pip3 install --upgrade pip
/home/pi/.virtualenvs/py3cv3/bin/pip3 install pydbus

http://www.adambowes-portfolio.com/blog/2014/11/3/thymio-ii-control-with-python

pi@raspberrypi:~ $ sudo asebamedulla "ser:name=Thymio-II"
Found Thymio-II on port /dev/ttyACM0

https://www.thymio.org/en:asebamedulla

```
('sys-devices-platform-soc-3f980000.usb-usb1-1\\x2d1-1\\x2d1.4-1\\x2d1.4:1.0-tty-ttyACM0.device', 'Thymio-II', 'loaded', 'active', 'plugged', '', '/org/freedesktop/systemd1/unit/sys_2ddevices_2dplatform_2dsoc_2d3f980000_2eusb_2dusb1_2d1_5cx2d1_2d1_5cx2d1_2e4_2d1_5cx2d1_2e4_3a1_2e0_2dtty_2dttyACM0_2edevice', 0, '', '/')
('dev-ttyACM0.device', 'Thymio-II', 'loaded', 'active', 'plugged', 'sys-devices-platform-soc-3f980000.usb-usb1-1\\x2d1-1\\x2d1.4-1\\x2d1.4:1.0-tty-ttyACM0.device', '/org/freedesktop/systemd1/unit/dev_2dttyACM0_2edevice', 0, '', '/')
('dev-serial-by\\x2did-usb\\x2dMobsya.org_Thymio\\x2dII\\x2dif00.device', 'Thymio-II', 'loaded', 'active', 'plugged', 'sys-devices-platform-soc-3f980000.usb-usb1-1\\x2d1-1\\x2d1.4-1\\x2d1.4:1.0-tty-ttyACM0.device', '/org/freedesktop/systemd1/unit/dev_2dserial_2dby_5cx2did_2dusb_5cx2dMobsya_2eorg_5fThymio_5cx2dII_5cx2dif00_2edevice', 0, '', '/')
('dev-serial-by\\x2dpath-platform\\x2d3f980000.usb\\x2dusb\\x2d0:1.4:1.0.device', 'Thymio-II', 'loaded', 'active', 'plugged', 'sys-devices-platform-soc-3f980000.usb-usb1-1\\x2d1-1\\x2d1.4-1\\x2d1.4:1.0-tty-ttyACM0.device', '/org/freedesktop/systemd1/unit/dev_2dserial_2dby_5cx2dpath_2dplatform_5cx2d3f980000_2eusb_5cx2dusb_5cx2d0_3a1_2e4_3a1_2e0_2edevice', 0, '', '/')

