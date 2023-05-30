#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and prints fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    while True:
        port = random.randint(1, 65535)
        print('Port {} is listening on {}'.format(port, fruits[port]))
        time.sleep(1)
        
