#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports. """    
    ports = range(1,65535)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work. 