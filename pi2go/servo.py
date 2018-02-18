# import RPi.GPIO as GPIO

# #set GPIO numbering mode and define output pins
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(15,GPIO.OUT)

# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)

# #gpio of servo = 15
# p = GPIO.PWM(15,50)
# p.start(7.5)

# def middle():
#     p.ChangeDutyCycle(7.5)

# def left():
#     p.ChangeDutyCycle(12.5) 

# def right():
#     p.ChangeDutyCycle(2.5)

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
pi2go.startServod()

try:
	pi2go.setServo(15,90)
	while True:
		keyp = readkey()
        if keyp == 'i':
        	pinServod(15,90)
            print 'Servo set to Middle Position'
        elif keyp == 'o':
        	pinServod(15,0)
            pi2go.reverse(speed)
            print 'Servo set to Left Position'
        elif keyp == 'p':
        	pinServod(15,180)
            pi2go.spinRight(speed)
            print 'Servo set to Right Position'

        # elif keyp == '.' or keyp == '>':
        #     speed = min(100, speed+10)
        #     print 'Speed+', speed
        # elif keyp == ',' or keyp == '<':
        #     speed = max (0, speed-10)
        #     print 'Speed-', speed

        # elif keyp == ' ':
        #     pi2go.stop()
        #     print 'Stop'

        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    pi2go.cleanup()
