#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or stores a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    if port == '/dev/ttyUSB0':
        port = '/dev/ttyUSB1'
    
    words = []
    
    try:
        with open(port, 'r') as port:
            for line in port:
                line = line.strip()
                
                if line == '':
                    continue
                
                words.append(line)
                
    except FileNotFoundError:
        print('Port not found')
        
    words = 