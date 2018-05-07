#!/usr/bin/env python3

import ev3

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
my_ev3.verbosity = 1

ops = b''.join([
    ev3.opUI_Draw,
    ev3.TOPLINE,
    ev3.LCX(0),     # ENABLE
    ev3.opUI_Draw,
    ev3.FILLWINDOW,
    ev3.LCX(0),     # COLOR
    ev3.LCX(0),     # Y0
    ev3.LCX(0),     # Y1
    ev3.opUI_Draw,
    ev3.UPDATE,
    ev3.opTimer_Wait,
    ev3.LCX(1000),
    ev3.LVX(0),
    ev3.opTimer_Ready,
    ev3.LVX(0),
    ev3.opUI_Draw,
    ev3.LINE,
    ev3.LCX(1),     # COLOR
    ev3.LCX(2),     # X0
    ev3.LCX(125),   # Y0
    ev3.LCX(88),    # X1
    ev3.LCX(2),     # Y1
    ev3.opUI_Draw,
    ev3.UPDATE,
    ev3.opTimer_Wait,
    ev3.LCX(500),
    ev3.LVX(0),
    ev3.opTimer_Ready,
    ev3.LVX(0),
    ev3.opUI_Draw,
    ev3.LINE,
    ev3.LCX(1),     # COLOR
    ev3.LCX(88),    # X0
    ev3.LCX(2),     # Y0
    ev3.LCX(175),   # X1
    ev3.LCX(125),   # Y1
    ev3.opUI_Draw,
    ev3.UPDATE,
    ev3.opTimer_Wait,
    ev3.LCX(500),
    ev3.LVX(0),
    ev3.opTimer_Ready,
    ev3.LVX(0),
    ev3.opUI_Draw,
    ev3.LINE,
    ev3.LCX(1),     # COLOR
    ev3.LCX(175),   # X0
    ev3.LCX(125),   # Y0
    ev3.LCX(2),     # X1
    ev3.LCX(125),   # Y1
    ev3.opUI_Draw,
    ev3.UPDATE
])
my_ev3.send_direct_cmd(ops, local_mem=4)