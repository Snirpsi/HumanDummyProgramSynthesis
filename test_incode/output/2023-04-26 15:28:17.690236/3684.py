#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    
    port = int(sys.argv[1])
    
    while True:
        
        # Wait for data
        data = sys.stdin.readline()
        
        # Print data
        print(data)
        
        # Send data
        sys.stdout.write("