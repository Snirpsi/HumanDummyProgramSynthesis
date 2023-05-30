#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and multiplyes fruits. """    
    ports = [int(i) for i in sys.argv[1:]]
    fruits = [int(f) for f in sys.argv[2:]]
    
    for port in ports:
        for fruit in fruits:
            print('Port {} Fruit {}'.format(port, fruit))
            
