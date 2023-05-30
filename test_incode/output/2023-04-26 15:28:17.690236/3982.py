#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and enumerates a port. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError:
        print('Usage: python ports.py [-h] [-o port] [-p port]')
        sys.exit(2)
    
    ports = []
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: python ports.py [-h] [-o port] [-p port]')
            sys.exit()
        elif opt in ('-o', '--port'):
            ports.append(arg)
        elif opt in ('-p', '--ports'):
            ports.extend(arg.split())
    
    if len(ports) == 0:
        print('Usage: python ports.py [-h] [-o port] [-p port]')
        sys.exit()
    
    for port in ports:
        port = int(port)
        
        if port in ports:
            print('Port {} is already in use'.format(port))
        else:
            print('Port {} is now in use'.format(port))
    
