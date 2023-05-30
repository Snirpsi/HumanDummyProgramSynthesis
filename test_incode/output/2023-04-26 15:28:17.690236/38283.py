#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and multiplyes fruits. """    
    ports = [
        Port("COM1", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
        Port("COM2", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
        Port("COM3", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
    ]
    fruits = [
        Apple("Apple", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
        Orange("Orange", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
        Banana("Banana", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE),
    ]
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    fruits[0].open()
    
    for port in ports:
        port.open()
    for fruit in fruits:
        fruit.open()
    
    ports[0].close()
    fruits[0].close()
    
    ports[0].open()
    