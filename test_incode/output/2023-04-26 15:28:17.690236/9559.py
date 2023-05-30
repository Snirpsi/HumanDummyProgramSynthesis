#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and converts fruits. """    
    port = 1
    while True:
        fruits = ['apple', 'banana', 'orange', 'kiwi']
        fruits.append(fruits.pop(random.randint(0, len(fruits)-1)))
        print('Port {}: {}'.format(port, fruits))
        port += 1
        time.sleep(1)
