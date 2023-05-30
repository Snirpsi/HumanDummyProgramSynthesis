#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and enumerates fruits. """    
    
    ports = range(65535)
    fruits = list('apple')
    
    for port in ports:
        print('serving on port {}'.format(port))
        
        for fruit in fruits:
            print('serving on port {} with fruit {}'
                  .format(port, fruit))
            
