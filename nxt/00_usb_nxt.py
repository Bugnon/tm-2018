##author: Raphael Holzer
##date: 2018-04-24
##file: 00_usb_nxt.py

import usb.core
import usb.util

##Install the USB module
##$pip3 install pyusb
##
##Verify its presence
##$pip3 list
##pyusb              1.0.2   

##You need to set up a udev rule (udev= linux devic manager)
##cd /etc/udev/rules.d/
##sudo nano ev3.rules
##ATTRS{idVendor}=="0694",ATTRS{idProduct}=="0005",MODE="0666",GROUP="pi"
##
##Restart udev with
##sudo udevadm trigger

##New error: usb.core.USBError: [Errno 16] Resource busy

##List the connected USB devices
##$lsusb
##Bus 001 Device 010: ID 0694:0005 Lego Group (Mindstorms EV3)
##Bus 001 Device 009: ID 0694:0002 Lego Group Mindstorms NXT

ID_VENDOR_LEGO = 0x0694
ID_PRODUCT_NXT = 0x0002
# find our device
dev = usb.core.find(idVendor=ID_VENDOR_LEGO, idProduct=ID_PRODUCT_NXT)
print(dev)



##sn = usb.util.get_string(dev, dev.iSerialNumber)
####print(sn)
##
##for cfg in dev:
##    print(cfg)
####    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
##
### was it found?
##if dev is None:
##    raise ValueError('Device not found')
##
### set the active configuration. With no arguments, the first
### configuration will be the active one
####dev.set_configuration()
##
### get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]
print(intf[1])


ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
##
##assert ep is not None
##
### write the data
##ep.write('test')