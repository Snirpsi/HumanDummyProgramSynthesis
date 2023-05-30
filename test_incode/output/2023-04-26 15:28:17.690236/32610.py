#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and enumerates a list of words. """    
    
    port = "/dev/ttyUSB0"
    words = []
    
    port = serial.Serial(port, 115200, timeout=1)
    port.flushInput()
    port.flushOutput()
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+CIPMUX=4\r\n")
    
    port.write("AT+CIPMUX=1\r\n")
    port.write("AT+CIPMUX=0\r\n")
    port.write("AT+CIPMUX=3\r\n")
    port.write("AT+