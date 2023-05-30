#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or multiplyes user input. """    
    ports = input("Enter ports: ")
    ports = ports.split()
    ports = [int(p) for p in ports]
    ports = [p*2 for p in ports]
    ports = [p for p in ports if p is not None]
    ports = " ".join(str(p) for p in ports)
    print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks, this was very helpful!
<|/ c |>
<| c |>
Glad it helped!
<|/ c |>
<| c |>
I 