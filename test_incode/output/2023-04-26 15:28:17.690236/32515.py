#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python {} <file> ...'.format(sys.argv[0]))
        sys.exit()
    
    for filename in sys.argv[1:]:
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            
            if len(line) == 0:
                continue
            
            number = int(line)
            
            if number < 0:
                print('Error: negative number in {}'.format(filename))
                sys.exit(1)
            
            if number > sys.maxsize:
                print('Error: number too big in {}'.format(filename))
                sys.exit(1)
            
            print('{}: {}'.format(number, line))
        
        file.close()
        
        print('')
        
