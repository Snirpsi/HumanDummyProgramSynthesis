#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or prints numbers. """    
    ports = range(1024)
    while True:
        for port in ports:
            print(port)
        time.sleep(1)
</code>
<|/ a dscore=1 |>
<| c |>
Thanks, I used your solution and it worked for me. 