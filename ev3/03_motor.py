#!/usr/bin/env python3

import curses
import ev3

def move(speed: int, turn: int) -> None:
    global myEV3, stdscr
    stdscr.addstr(5, 0, 'speed: {}, turn: {}      '.format(speed, turn))
    if turn > 0:
        speed_right = speed
        speed_left  = round(speed * (1 - turn / 100))
    else:
        speed_right = round(speed * (1 + turn / 100))
        speed_left  = speed
    ops = b''.join([
        ev3.opOutput_Speed,
        ev3.LCX(0),                       # LAYER
        ev3.LCX(ev3.PORT_B),              # NOS
        ev3.LCX(speed_right),             # SPEED
        ev3.opOutput_Speed,
        ev3.LCX(0),                       # LAYER
        ev3.LCX(ev3.PORT_C),              # NOS
        ev3.LCX(speed_left),              # SPEED
        ev3.opOutput_Start,
        ev3.LCX(0),                       # LAYER
        ev3.LCX(ev3.PORT_B + ev3.PORT_C)  # NOS
    ])
    myEV3.send_direct_cmd(ops)

def stop() -> None:
    global myEV3, stdscr
    stdscr.addstr(5, 0, 'vehicle stopped                         ')
    ops = b''.join([
        ev3.opOutput_Stop,
        ev3.LCX(0),                       # LAYER
        ev3.LCX(ev3.PORT_B + ev3.PORT_C), # NOS
        ev3.LCX(0)                        # BRAKE
    ])
    myEV3.send_direct_cmd(ops)

def react(c):
    global speed, turn
    if c in [ord('q'), 27, ord('p')]:
        stop()
        return
    elif c == curses.KEY_LEFT:
        turn += 5
        turn = min(turn, 200)
    elif c == curses.KEY_RIGHT:
        turn -= 5
        turn = max(turn, -200)
    elif c == curses.KEY_UP:
        speed += 5
        speed = min(speed, 100)
    elif c == curses.KEY_DOWN:
        speed -= 5
        speed = max(speed, -100)
    move(speed, turn)

def main(window) -> None:
    global stdscr
    stdscr = window
    stdscr.clear()      # print introduction
    stdscr.refresh()
    stdscr.addstr(0, 0, 'Use Arrows to navigate your EV3-vehicle')
    stdscr.addstr(1, 0, 'Pause your vehicle with key <p>')
    stdscr.addstr(2, 0, 'Terminate with key <q>')

    while True:
        c = stdscr.getch()
        if c in [ord('q'), 27]:
            react(c)
            break
        elif c in [ord('p'),
                   curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            react(c)

speed = 0
turn  = 0   
myEV3 = ev3.EV3(protocol=ev3.USB, host='00:16:53:49:CA:06')
stdscr = None

# ops = opOutput_Polarity + b'\x00' + LCX(PORT_A + PORT_D) + LCX(-1)
# myEV3.send_direct_cmd(ops)

curses.wrapper(main)