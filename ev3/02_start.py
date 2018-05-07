#!/usr/bin/env python3

import ev3

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
my_ev3.verbosity = 1

ops = b''.join([
    ev3.opFile,
    ev3.LOAD_IMAGE,
    ev3.LCX(1),                                         # SLOT
    ev3.LCS('../apps/Motor Control/Motor Control.rbf'), # NAME
    ev3.LVX(0),                                         # SIZE
    ev3.LVX(4),                                         # IP*
    ev3.opProgram_Start,
    ev3.LCX(1),                                         # SLOT
    ev3.LVX(0),                                         # SIZE
    ev3.LVX(4),                                         # IP*
    ev3.LCX(0)                                          # DEBUG
])
my_ev3.send_direct_cmd(ops, local_mem=8)