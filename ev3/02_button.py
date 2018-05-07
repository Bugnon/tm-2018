#!/usr/bin/env python3

import ev3

my_ev3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
my_ev3.verbosity = 1

ops = b''.join([
    ev3.opUI_Button,
    ev3.PRESS,
    ev3.BACK_BUTTON,
    ev3.opUI_Button,
    ev3.WAIT_FOR_PRESS,
    ev3.opUI_Button,
    ev3.PRESS,
    ev3.RIGHT_BUTTON,
    ev3.opUI_Button,
    ev3.WAIT_FOR_PRESS,
    ev3.opUI_Button,
    ev3.PRESS,
    ev3.ENTER_BUTTON
])
my_ev3.send_direct_cmd(ops)