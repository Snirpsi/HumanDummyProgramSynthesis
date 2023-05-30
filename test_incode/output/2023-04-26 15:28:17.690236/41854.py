#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or returns fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        
        print('Serving on port 8080')
        
    elif port == 5000:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        
        print('Serving on port 5000')
        
    else:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        
        print('Serving on port 8080')
        
        print('Fruits:')
        
        for fruit in fruits:
            print(