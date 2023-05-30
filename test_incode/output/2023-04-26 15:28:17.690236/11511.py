#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or multiplyes a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port == 0 or port == 65535:
            ports = range(1,65535)
        else:
            ports = range(1,port)
    else:
        ports = range(1,65535)
    
    for port in ports:
        
        port = str(port)
        
        if port == '0':
            port = '-1'
        
        print('Port: ' + str(port))
        print('Multiplication: ' + str(port*2))
        
        print('Port: ' + str(port) + ' (original)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('Port: ' + str(port) + ' (modified)')
        print('Multiplication: ' + str(port*2) + ' (modified)')
        
        print('