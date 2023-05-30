#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or converts a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Port must be between 0 and 65535.")
        sys.exit()
    
    portstr = str(port)
    
    if portstr == '0': 
        portstr = '00'
    
    if portstr == '1': 
        portstr = '01'
    
    if portstr == '2': 
        portstr = '02'
    
    if portstr == '3': 
        portstr = '03'
    
    if portstr == '4': 
        portstr = '04'
    
    if portstr == '5': 
        portstr = '05'
    
    if portstr == '6': 
        portstr = '06'
    
    if portstr == '7': 
        portstr = '07'
    
    if portstr == '8': 
        portstr = '08'
    
    if portstr == '9': 
        portstr = '09'
    
    if portstr == 'A': 
        portstr = '0A'
    
    if portstr == 'B': 
        portstr = '0B'
    
    if portstr == 'C': 
        portstr = '0C'
    
    if portstr == 'D': 
        portstr = '0D'
    
    if portstr == 'E': 
        portstr = '0E'
    
    if portstr == 'F': 
        portstr = '0F'
    
    if portstr == 'G': 
        portstr = '10'
    
    if portstr == 'H': 
        portstr = '11'
    
    if portstr == 'I': 
        portstr = '12'
    
    if portstr == 'J': 
        portstr = '13'
    
    if portstr == 'K': 
        portstr = '14'
    
    if portstr == 'L': 
        portstr = '15'
    
    if portstr == 'M': 
        portstr = '16'
    
    if portstr == 'N': 
        portstr = '17'
    
    if portstr == 'O': 
        portstr = '18'
    
    if portstr == 'P': 
        portstr = '19'
    
    if portstr == 'Q': 
        portstr = '1A'
    
    if portstr == 'R': 
        portstr = '1B'
    
    if portstr == 'S': 
        portstr = '1C'
    
    if portstr == 'T': 
        port