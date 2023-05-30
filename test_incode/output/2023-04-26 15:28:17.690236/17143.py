#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 number2string.py <number>")
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 0:
        print("Error: negative numbers are not allowed")
        sys.exit()
    
    string = ""
    
    while number > 0:
        string = string + str(number%10) + " "
        number //= 10
    
    print(string)

<|/ file ext=.py source=github |>