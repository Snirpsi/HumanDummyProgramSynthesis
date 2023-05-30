#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python number_to_store.py <number> [<number> ...]")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        
        try:
            number = int(number)
        except ValueError:
            print("Error: number must be an integer")
            sys.exit()
        
        store