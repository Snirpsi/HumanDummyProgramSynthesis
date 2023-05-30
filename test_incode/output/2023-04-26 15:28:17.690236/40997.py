#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or removes a port. """    
    
    port = int(sys.argv[1])
    
    if sys.argv[2] == 'add':
        numbers = sys.argv[3:]
        
        for number in numbers:
            number = int(number)
            
            ports.append(number)
            
    elif sys.argv[2] == 'remove':
        numbers = sys.argv[3:]
        
        for number in numbers:
            number = int(number)
            
            ports.remove(number)
            
    else:
        print('Usage: %s add <port> [<port>]' % sys.argv[0])
        
