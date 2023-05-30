#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    number = int(number)
    
    if number < 0:
        print("Negative numbers are not allowed!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Number cannot be empty!")
        sys.exit()
    
    number = number.replace('-', '')
    number = number.replace('+', '')
    number = number.replace(' ', '')
    number = number.replace(',', '')
    
    number = int(number)
    
    if number == 0:
        print("Number cannot be 0!")
        sys.exit()
    
    number = str(number)
    
    if number 