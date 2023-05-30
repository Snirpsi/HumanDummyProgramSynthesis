#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    removed = remove_list(numbers)
    
    if removed:
        print("Removed %d numbers" % len(removed))
    else:
        print("No numbers removed")
    
