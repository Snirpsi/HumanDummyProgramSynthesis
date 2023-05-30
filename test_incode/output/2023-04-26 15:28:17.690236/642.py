#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or returns a list of words. """    
    import sys
    if len(sys.argv) > 1:
        number = sys.argv[1]
    else:
        number = input("Enter a number: ")
    
    try:
        number = int(number)
    except ValueError:
        print("Invalid number")
        sys.exit()
    
    if number == 0:
        print("0")
        sys.exit()
    
    if number == 1:
        print("1")
        sys.exit()
    
    words = []
    
    for i in range(number):
        words.append(str(i))
    
    print(" ".join(words))
    
