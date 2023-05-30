#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    port = '/dev/ttyUSB0'
    
    ports = serial.tools.list_ports.comports()
    
    for port in ports:
        if port.device == 'ttyUSB0':
            
            baud = port.baudrate
            
            baud_str = str(baud)
            
            baud_str = baud_str.replace(' ', '')
            
            baud_str = baud_str.replace(',', '')
            
            baud_str = baud_str.replace('.', '')
            
            baud_str = baud_str.replace('-', '')
            
            baud_str = baud_str.replace(':', '')
            
            baud_str = baud_str.replace(';', '')
            
            baud_str = baud_str.replace('?', '