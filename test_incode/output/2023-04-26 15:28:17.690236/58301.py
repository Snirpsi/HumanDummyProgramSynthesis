#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python number_generator.py <n>')
        sys.exit()
    
    n = int(sys.argv[1])
    
    for i in range(n):
        print(i)
        
