#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or stores fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        fruits = Fruits(8080)
        fruits.serve()
    elif port == 8000:
        fruits = Fruits(8000)
        fruits.serve()
    else:
        fruits = Fruits(port)
        fruits.serve()
        
