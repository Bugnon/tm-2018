import pydbus
from pydbus import SystemBus

bus = SystemBus()
systemd = bus.get(".systemd1")

##for unit in systemd.ListUnits():
##    print(unit)


# gets stub of ASEBA asebaNetwork
##bus = pydbus.SessionBus()
bus = pydbus.SystemBus()
asebaNetworkObject = bus.get("ch.epfl.mobots.Aseba", "/")
print(asebaNetworkObject)
##asebaNetwork = pydbus.Interface(asebaNetworkObject, dbus_interface="ch.epfl.mobots.AsebaNetwork")
