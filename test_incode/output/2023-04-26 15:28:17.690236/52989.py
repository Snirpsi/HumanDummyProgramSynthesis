#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port. """    
    
    while True:
        port = random.randint(10000, 30000)
        
        print("Port is: " + str(port))
        
        time.sleep(10)
        
