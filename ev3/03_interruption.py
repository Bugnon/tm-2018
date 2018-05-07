#!/usr/bin/env python3

import ev3, time

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')

ops = b''.join([
    ev3.opUI_Write,
    ev3.LED,
    ev3.LED_RED,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(262),
    ev3.LCX(0)
])
my_ev3.send_direct_cmd(ops)
time.sleep(0.5)
ops = b''.join([
    ev3.opUI_Write,
    ev3.LED,
    ev3.LED_GREEN,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(330),
    ev3.LCX(0)
])
my_ev3.send_direct_cmd(ops)
time.sleep(0.5)
ops = b''.join([
    ev3.opUI_Write,
    ev3.LED,
    ev3.LED_RED,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(392),
    ev3.LCX(0)
])
my_ev3.send_direct_cmd(ops)
time.sleep(0.5)
ops = b''.join([
    ev3.opUI_Write,
    ev3.LED,
    ev3.LED_RED_FLASH,
    ev3.opSound,
    ev3.TONE,
    ev3.LCX(1),
    ev3.LCX(523),
    ev3.LCX(0)
])
my_ev3.send_direct_cmd(ops)
time.sleep(2)
ops = b''.join([
    ev3.opUI_Write,
    ev3.LED,
    ev3.LED_GREEN,
    ev3.opSound,
    ev3.BREAK
])
my_ev3.send_direct_cmd(ops)