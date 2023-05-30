#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and iterates over a port. """    
    port = int(sys.argv[1])
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    while(True):
        words = words * port
        
        for word in words:
            print(word)
        
        time.sleep(1)
        
