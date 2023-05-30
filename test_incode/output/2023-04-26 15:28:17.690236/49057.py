#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and converts a list of words. """    
    port = '/dev/ttyUSB0'
    words = ['hello', 'world']
    
    # Open the port and read each word as a separate line
    lines = port.read().splitlines()
    
    # Iterate over the lines and print each line as a separate word
    for line in lines:
        for word in words:
            print(word + ' ' + line)
            
    # Close the port and exit
    port.close()
    
    # 