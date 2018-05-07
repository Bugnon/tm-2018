#!/usr/bin/env python3

import ev3

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
my_ev3.verbosity = 1
ops = b''.join([
    ev3.opCom_Set,
    ev3.SET_BRICKNAME,
    ev3.LCS("myEV3")
])
my_ev3.send_direct_cmd(ops)