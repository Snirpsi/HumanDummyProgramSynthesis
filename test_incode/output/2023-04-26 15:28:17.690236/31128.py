#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or prints numbers. """    
    import sys
    
    words = []
    numbers = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    if len(words) == 0:
        words = ['the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', 'a', 'an', 'and', 'the', '