#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and stores user input. """    
    
    ports = [
        port for port in os.listdir('/dev/tty