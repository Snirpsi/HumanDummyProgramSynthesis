#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or calculates all ports. """    
    
    fruit = sys.argv[1]
    
    if fruit == 'fruit':
        fruit()
    elif fruit == 'ports':
        ports()
    else:
        print('Unknown fruit 