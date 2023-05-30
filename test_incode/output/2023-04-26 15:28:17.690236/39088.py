#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(str(number))
        else:
            number = int(input("Enter a number: "))
            
            if number > 0:
                print(str(number))
            else:
                print("Invalid number")
    else:
        print("Usage: python wordlist.py [number]")
    
