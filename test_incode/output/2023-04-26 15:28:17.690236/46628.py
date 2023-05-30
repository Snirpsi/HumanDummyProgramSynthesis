#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port and opens fruits. """    
    port = int(input('Enter a port: '))
    fruits = open('fruits.txt', 'w')
    fruits.write(str(port))
    fruits.close()
    print('The port is ' + str(port))
    
