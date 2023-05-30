#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python remove_numbers.py <file_to_remove>")
        sys.exit()
    
    remove