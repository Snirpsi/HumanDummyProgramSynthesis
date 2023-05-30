#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or enumerates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python store.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    store = Store()
    
    for number in numbers:
        store.add(number)
    
    print(store.