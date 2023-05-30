#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <number> <output>' % sys.argv[0])
        sys.exit(1)
    
    number = sys.argv[1]
    output = sys.argv[2]
    
    number = int(number)
    output = open(output, 'w')
    
    output.write('%d\t%s\n' % (number, number))
    output.close()
    
