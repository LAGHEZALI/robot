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

pi2go.init()

cycle = 7.5

try:
	while True:
		keyp = readkey()
		if keyp == 'i':
			pi2go.servoMiddle()
			print 'Servo set to Middle Position'
		elif keyp == 'o':
			pi2go.servoLeft()
			print 'Servo set to Left Position'
		elif keyp == 'p':
			pi2go.servoRight()
			print 'Servo set to Right Position'
		elif odr(keyp) == 3:
			break

        elif keyp == '.':
            cycle +=0.5
            pi2go.setServoCycle(cycle)
            print 'Servo Cycle ++ = ', cycle
        elif keyp == ',':
            cycle -=0.5
            pi2go.setServoCycle(cycle)
            print 'Servo Cycle -- = ', cycle

        elif keyp == ' ':
            pi2go.stopServo()
            print 'Stop Servo'

except KeyboardInterrupt:
	pi2go.stopServo()
    pi2go.cleanup()
