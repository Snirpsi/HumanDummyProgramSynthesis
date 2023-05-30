#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 convert.py <number>")
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 0:
        print("Error: number must be positive.")
        sys.exit()
    
    number = abs(number)
    
    number = int(number)
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 10
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 100
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 1000
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 10000
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 100000
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 1000000
    
    if number % 10 == 0:
        print("The number is a multiple of ten.")
    elif number % 100 == 0:
        print("The number is a multiple of hundred.")
    elif number % 1000 == 0:
        print("The number is a multiple of thousand.")
    else:
        print("The number is a multiple of one.")
    
    number = number / 10000000
