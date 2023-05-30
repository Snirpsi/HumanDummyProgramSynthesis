#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python store.py <filename>')
        exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'w') as f:
        f.write('')
        
    print('Stored numbers in {}'.format(filename))
    
