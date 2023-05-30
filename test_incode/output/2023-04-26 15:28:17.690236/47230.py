#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or stores all ports. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    print('\n'.join(ports))
</code>
<|/ a tags=python-3.x,python,python-2.7 |>
<| c |>
Thank you very much! This works perfectly. 