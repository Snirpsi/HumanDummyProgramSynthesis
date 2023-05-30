#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or returns a list of numbers. """    
    
    ports = ports_converter(sys.argv[1])
    
    if ports:
        print('\n'.join(ports))
    else:
        print('No ports found')
        
