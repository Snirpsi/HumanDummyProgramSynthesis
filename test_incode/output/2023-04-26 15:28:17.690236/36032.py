#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and opens fruits. """    
    
    port = 0
    while True:
        port += 1
        
        print('Starting port {}...'.format(port))
        
        fruits = open('fruits.txt', 'w')
        fruits.write('Fruit {}\n'.format(port))
        fruits.close()
        
        print('Port {} is open!'.format(port))
        
        time.sleep(1)
        
        print('Closing port {}...'.format(port))
        
        fruits.close()
        
        print('Port {} is closed!'.format(port))
        
