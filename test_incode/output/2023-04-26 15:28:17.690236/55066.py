#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        port = str(port)
        
        if port == '':
            continue
        
        if port == '1':
            port = '/dev/ttyUSB0'
        
        if port == '2':
            port = '/dev/ttyUSB1'
        
        if port == '3':
            port = '/dev/ttyUSB2'
        
        if port == '4':
            port = '/dev/ttyUSB3'
        
        if port == '5':
            port = '/dev/ttyUSB4'
        
        if port == '6':
            port = '/dev/ttyUSB5'
        
        if port == '7':
            port = '/dev/ttyUSB6'
        
        if port == '8':
            port = '/dev/ttyUSB7'
        
        if port == '9':
            port = '/dev/ttyUSB8'
        
        if port == '10':
            port = '/dev/ttyUSB9'
        
        if port == '11':
            port = '/dev/ttyUSB10'
        
        if port == '12':
            port = '/dev/ttyUSB11'
        
        if port == '13':
            port = '/dev/ttyUSB12'
        
        if port == '14':
            port = '/dev/ttyUSB13'
        
        if port == '15':
            port = '/dev/ttyUSB14'
        
        if port == '16':
            port = '/dev/ttyUSB15'
        
        if port == '17':
            port = '/dev/ttyUSB16'
        
        if port == '18':
            port = '/dev/ttyUSB17'
        
        if port == '19':
            port = '/dev/ttyUSB18'
        
        if port == '20':
            port = '/dev/ttyUSB19'
        
        if port == '21':
            port = '/dev/ttyUSB20'
        
        if port == '22':
            port = '/dev/ttyUSB21'
        
        if port == '23':
            port = '/dev/ttyUSB22'
        
        if port == '24':
            port = '/dev/ttyUSB23'
        
        if port == '25':
            port = '/dev/ttyUSB24'
        
        if port == '26':
            port = '/dev/ttyUSB25'
        
        if port == '27':