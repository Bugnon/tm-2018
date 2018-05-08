import usb

ID_VENDOR_LEGO = 0x0694
ID_PRODUCT_NXT = 0x0002
# find our device
dev = usb.core.find(idVendor=ID_VENDOR_LEGO, idProduct=ID_PRODUCT_NXT)
print(dev)