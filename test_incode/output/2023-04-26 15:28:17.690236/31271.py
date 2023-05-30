#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and adds a port. """    
    port = random.randint(10000, 30000)
    webserver.run(port)

<|/ file ext=.py source=github |>