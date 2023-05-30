#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and adds all ports. """    
    ports = []
    while True:
        ports.append(get_port())
        time.sleep(1)
        
    print("All ports found!")
    
    
<|/ file ext=.py source=github |>