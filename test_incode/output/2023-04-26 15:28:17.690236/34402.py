#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or calculates numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world', 'python', 'is', 'cool']
    
    for word in words:
        print(word)
        
