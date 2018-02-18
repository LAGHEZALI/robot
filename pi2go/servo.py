import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

p = GPIO.PWM(15,50)
p.start(7.5)

def middle():
    p.ChangeDutyCycle(7.5)

def left():
    p.ChangeDutyCycle(12.5) 

def right():
    p.ChangeDutyCycle(2.5)

try:
    middle()
    while True:
        char = screen.getch()
        if char == ord(' '):
            break
        elif char == ord('i'):
            middle()
        elif char == ord('o'):
            left()
        elif char == ord('p'):
        	right()

finally:
    curses.nocbreak();screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
