#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and removes a port. """    
    ports = input("Enter the ports you want to remove: ")
    ports = ports.split(",")
    for port in ports:
        ports.remove(port)
    print(ports)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This code will remove all ports, not just those that are in the input. OP wants to remove all ports except those in the input.
<|/ c |>
<| c |>
I updated my answer to include a solution to remove all ports except those in the input
<|/ c |>
<| c |>
This code will remove all ports, not just those that are in the input. OP wants to remove all ports except those in the input.
<|/ c |>
<| c |>
I updated my answer to include a solution to remove all ports except those in the input
<|/ c |>
<| c |>
This code will remove all ports, not just those that are in the input. OP wants to remove all ports except those in the input.
<|/ c |>
<| a dscore=0 |>
<code>
ports = input("Enter the ports you want to remove: ")
ports = ports.split(",")
ports = [p for p in ports if p not in ports]
print(ports)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This code will remove all ports, not just those that are in the input. OP wants to remove all ports except those in the input.
<|/ c |>
<| c |>
I updated my answer to include a solution to remove all ports except those in the input
<|/ c |>
<| a tags=python,python-3.x |>
<code>
ports = input("Enter the ports you want to remove: ")
ports = ports.split(",")
ports = [p for p in ports if p not in ports]
print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
This code will remove all ports, not just those that are in the input. OP wants to remove all ports except those in the input.
<|/ c |>
<| a dscore=0 |>
<code>
ports = input("Enter the ports you want to remove: ")
ports = ports.split(",")
ports = [p for p in ports if p not in ports]
print(ports)
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 |>
<code>
ports = input("Enter the ports you want to remove: ")
ports = ports.split(",")
ports = [p for 