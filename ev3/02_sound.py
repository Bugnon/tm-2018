#!/usr/bin/env python3

import ev3, time

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
my_ev3.verbosity = 1

ops = b''.join([
    ev3.opSound,
    ev3.PLAY,
    ev3.LCX(100),                  # VOLUME
    ev3.LCS('./ui/DownloadSucces') # NAME
])
my_ev3.send_direct_cmd(ops)

ops = b''.join([
    ev3.opSound,
    ev3.REPEAT,
    ev3.LCX(50),                  # VOLUME
    ev3.LCS('./ui/DownloadSucces') # NAME
])
my_ev3.send_direct_cmd(ops)
time.sleep(3)
ops = b''.join([
    ev3.opSound,
    ev3.BREAK
])
my_ev3.send_direct_cmd(ops)

ops = b''.join([
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),    # VOLUME
    ev3.LCX(440),  # FREQUENCY
    ev3.LCX(1000), # DURATION
])
my_ev3.send_direct_cmd(ops)

ops = b''.join([
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(262),
    ev3.LCX(500),
    ev3.opSound_Ready,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(330),
    ev3.LCX(500),
    ev3.opSound_Ready,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(392),
    ev3.LCX(500),
    ev3.opSound_Ready,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(2),
    ev3.LCX(523),
    ev3.LCX(1000)
])
my_ev3.send_direct_cmd(ops)