# Controlling the LEGO MINDSTORMS NXT with the Raspberry Pi

## Configure Chromium to display Markdown files
* Chrome > Extensions > Get more extensions
* add Markdown Viewer
* Chrome > Extensiosn > Markdown Viewer
* check Allow acces to file URLs
* Restart Chromium


## Configure Thonny
* Thonny > Tools > Options > Interpreter
* Locate another executable
* /home/pi/.virtualenvs/py3cv3/bin/python3

Test
```
>>> Python 3.4.2 (/home/pi/.virtualenvs/py3cv3/bin/python3)
>>> import cv2
>>>
```
## Upgrade the package installer pip
```
/home/pi/.virtualenvs/py3cv3/bin/pip3 install --upgrade pip
```

## Install pyusb module
* Thonny > Tools > Open system shell...
* /home/pi/.virtualenvs/py3cv3/bin/pip3 install pyusb

Test
```
>>> import usb
>>>
```

## Check if LEGO MINESTORMS is visible
```
$ lsusb
Bus 001 Device 004: ID 0694:0002 Lego Group Mindstorms NXT
...
```

## Set up a udev rule (udev= linux devic manager)
```
$ cd /etc/udev/rules.d/
$ sudo nano ev3.rules
ATTRS{idVendor}=="0694",ATTRS{idProduct}=="0005",MODE="0666",GROUP="pi"

$ sudo udevadm trigger
```

## Install nxt-python module
* https://github.com/Eelviny/nxt-python
* Clone or download > Download ZIP
* Go to Downloads
* Right-click on nxt-python-master.zip > Extract Here
```
$ cd /home/pi/Downloads/nxt-python-master
$ cp -r nxt /home/pi/.virtualenvs/py3cv3/lib/python3.4/site-packages
```

Test
```
>>> import nxt
>>>
```

## Make /home/pi/.nxt-python config file
```
>>> nxt.locator.make_config()
Welcome to the nxt-python config file generator!
This function creates an example file which find_one_brick uses to find a brick.
The file has been written at /home/pi/.nxt-python
The file contains less-than-sane default values to get you started.
You must now edit the file with a text editor and change the values to match what you would pass to find_one_brick
The fields for name, host, and strict correspond to the similar args accepted by find_one_brick
The method field contains the string which would be passed to Method()
Any field whose corresponding option does not need to be passed to find_one_brick should be commented out (using a # at the start of the line) or simply removed.
If you have questions, check the wiki and then ask on the mailing list.
>>> 
```

Edit config file
```
[Brick]
name = NXT
host = 00:16:53:05:BB:77
strict = 0
method = usb=True, bluetooth=False
```