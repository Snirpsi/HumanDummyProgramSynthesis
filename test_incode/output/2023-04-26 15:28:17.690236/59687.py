#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = sys.argv[1:]
    ports = [int(p) for p in ports]
    
    ports_sum = 0
    for p in ports:
        ports_sum += p
    
    print('Ports sum:', ports_sum)
    
