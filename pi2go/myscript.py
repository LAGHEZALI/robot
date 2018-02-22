import pi2go, time

import sys
import tty
import termios

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

speed = 100
position = 50 # between 0 and 100
step = 2

pi2go.init()

try:
    while True:
        keyp = readkey()
        if keyp == 'w' or keyp == UP:
            pi2go.forward(speed)
            print 'Forward', speed
        elif keyp == 's' or keyp == DOWN:
            pi2go.reverse(speed)
            print 'Backward', speed
        elif keyp == 'd' or keyp == RIGHT:
            pi2go.spinRight(speed)
            print 'Spin Right', speed
        elif keyp == 'a' or keyp == LEFT:
            pi2go.spinLeft(speed)
            print 'Spin Left', speed

        elif keyp == '.' or keyp == '>':
            speed = min(100, speed+10)
            print 'Speed+', speed
        elif keyp == ',' or keyp == '<':
            speed = max (0, speed-10)
            print 'Speed-', speed

        elif keyp == ' ':
            pi2go.stop()
            print 'Stop Motors'

        if keyp == 'i':
            position = 50
            pi2go.setServo(position)
            print 'Servo set to Middle Position'
        elif keyp == 'o':
            position = 0
            pi2go.setServo(position)
            print 'Servo set to Left Position'
        elif keyp == 'p':
            position = 100
            pi2go.setServo(position)
            print 'Servo set to Right Position'
        
        elif keyp == 'y':
            if position<100:
                position +=step
                pi2go.setServo(position)
                print 'Servo Position +', step, '=', position
        elif keyp == 'u':
            if position>0:
                position -=step
                pi2go.setServo(position)
                print 'Servo Position -', step, '=', position
        elif keyp == 't':
            pi2go.stopServo()
            print 'Stop Servo'

        elif keyp == 'x':
            break

except KeyboardInterrupt:
    pi2go.stop()
    pi2go.stopServo()
    pi2go.cleanup()
