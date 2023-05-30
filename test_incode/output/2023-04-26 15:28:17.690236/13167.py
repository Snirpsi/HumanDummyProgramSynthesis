#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or iterates over a port. """    
    
    # Open a port and iterate over all words in it
    port = serial.Serial('COM3', 9600, timeout=1)
    
    # Iterate over all words in port
    for word in port.readlines():
        print(word)
        
    # Close the port
    port.close()
    
    # Close the program
    