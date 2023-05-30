#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 number_to_word.py <number>")
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 0:
        print("Error: Negative numbers are not allowed")
        sys.exit()
    
    word = ""
    
    while number > 0:
        word = word + str(number % 10)
        number //= 10
    
    print(word)
    
