#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    while True:
        print("Enumerating numbers...")
        
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        for i, num in enumerate(numbers):
            print("%d\t%s" % (i, num))
        
        print("\nPress enter to exit.")
        
        input()
        
