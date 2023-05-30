#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or iterates over numbers. """    
    
    fruits = open('fruits.txt', 'r')
    
    while True:
        line = fruits.readline()
        
        if line == '':
            break
        
        number = int(line)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number * 2)
        
    fruits.close()
    
