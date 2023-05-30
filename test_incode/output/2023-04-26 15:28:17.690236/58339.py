#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or multiplyes all ports. """    
    ports = input("Enter ports separated by comma: ").split(",")
    ports = [int(port) for port in ports]
    ports = [port * 2 for port in ports]
    print(ports)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you very much! It works perfectly now!
<|/ c |>
<| c |>
You're welcome. Don't forget to accept the answer if it helped you.
<|/ c |>
<| a dscore=0 |>
<code>
