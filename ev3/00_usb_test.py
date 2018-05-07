import usb.core
import usb.util

##Install the USB module
##$pip3 install pyusb
##
##Verify its presence
##$pip3 list

##You need to set up a udev rule
##sudo nano ev3.rules
##ATTRS{idVendor}=="0694",ATTRS{idProduct}=="0005",MODE="0666",GROUP="pi"
##
##Restart udev with
##sudo udevadm trigger

##New error: usb.core.USBError: [Errno 16] Resource busy

##List the connected USB devices
##$lsusb
##Bus 001 Device 012: ID 0617:000a Swiss Federal Insitute of Technology (Thymio)
##Bus 001 Device 007: ID 05ac:020c Apple, Inc. Extended Keyboard [Mitsumi] 
##Bus 001 Device 013: ID 0694:0005 Lego Group (EV3)
   

# find our device
dev = usb.core.find(idVendor=0x0694)
print(dev)
sn = usb.util.get_string(dev, dev.iSerialNumber)
print(sn)

##for cfg in dev:
##    print(cfg)
##    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
##dev.set_configuration()

# get an endpoint instance
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

assert ep is not None

# write the data
ep.write('test')