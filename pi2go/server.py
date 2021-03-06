import pi2go, time
import sys
import tty
import termios
from socket import *

pi2go.init()

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print 'Waiting for connection'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :', addr
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        pi2go.setServo(int(data))
                        print 'Servo Position', '=', int(data)
        except KeyboardInterrupt:
                pi2go.stopServo()
                pi2go.cleanup()
tcpSerSock.close();