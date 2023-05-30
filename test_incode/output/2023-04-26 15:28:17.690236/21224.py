#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and enumerates words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    words = []
    
    for i in range(number):
        words.append(str(i))
    
    for word in words:
        print(word)
    
