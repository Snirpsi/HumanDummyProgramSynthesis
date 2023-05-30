#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers or iterates over all ports. """    
    
    # Add ports
    ports = [
        Port('COM1', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM2', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM3', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM4', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM5', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM6', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM7', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM8', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM9', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM10', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM11', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM12', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM13', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM14', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM15', baudrate=9600, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE),
        Port('COM16', baudrate=9600, parity=serial.PARITY_EVEN, stopbit