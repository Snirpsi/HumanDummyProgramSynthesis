#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or calculates words. """    
    port = 0
    while True:
        port = random.randint(10000, 20000)
        time.sleep(1)
        print(port)
        
<|/ file filename=