#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or prints fruits. """    
    while True:
        port = int(input('Port: '))
        if port == -1:
            break
        
        fruit = input('Fruit: ')
        if fruit == 'quit':
            break
        
        print('Fruit: {}'.format(fruit))
        
