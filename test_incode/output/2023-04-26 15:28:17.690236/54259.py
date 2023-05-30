#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 convert.py <number>")
        exit(1)
        
    number = int(sys.argv[1])
    
    if number < 0:
        print("Error: number must be positive.")
        exit(1)
    
    number = abs(number)
    
    if number > 1000:
        print("Error: number too large.")
        exit(1)
    
    number = int(number)
    
    number = number / 100
    
    number = number % 100
    
    number = number / 10
    
    number = number % 10
    
    number = number / 1
    
    number = number % 1
    
    number = number / 2
    
    number = number % 2
    
    number = number / 3
    
    number = number % 3
    
    number = number / 4
    
    number = number % 4
    
    number = number / 5
    
    number = number % 5
    
    number = number / 6
    
    number = number % 6
    
    number = number / 7
    
    number = number % 7
    
    number = number / 8
    
    number = number % 8
    
    number = number / 9
    
    number = number % 9
    
    number = number / 10
    
    number = number % 10
    
    number = number / 11
    
    number = number % 11
    
    number = number / 12
    
    number = number % 12
    
    number = number / 13
    
    number = number % 13
    
    number = number / 14
    
    number = number % 14
    
    number = number / 15
    
    number = number % 15
    
    number = number / 16
    
    number = number % 16
    
    number = number / 17
    
    number = number % 17
    
    number = number / 18
    
    number = number % 18
    
    number = number / 19
    
    number = number % 19
    
    number = number / 20
    
    number = number % 20
    
    number = number / 21
    
    number = number % 21
    
    number = number / 22
    
    number = number % 22
    
    number = number / 23
    
    number = number % 23
    
    number = number / 24
    
    number = number % 24
    
    number = number / 25
    
    number = number % 25
    