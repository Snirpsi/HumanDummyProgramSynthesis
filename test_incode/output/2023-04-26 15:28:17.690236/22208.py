#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python add.py <num1> <num2> ... <numN>')
        sys.exit()
    
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    for i in range(3, len(sys.argv)):
        num1 = int(sys.argv[i])
        num2 = int(sys.argv[i+1])
        
        num3 = num1 + num2
        
        print('%d + %d = %d' % (num1, num2, num3))
    
