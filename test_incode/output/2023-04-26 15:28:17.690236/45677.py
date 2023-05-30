#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or prints numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'words':
            
            words = [line.strip() for line in open('words.txt')]
            
            print('\n'.join(words))
            
        elif sys.argv[1] == 'numbers':
            
            numbers = [int(line) for line in open('numbers.txt')]
            
            print('\n'.join(map(str, numbers)))
            
        else:
            
            print('Usage: python server.py words|numbers')
            
    else:
        
        print('Usage: python server.py words|numbers')
        
