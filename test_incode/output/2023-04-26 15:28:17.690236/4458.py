#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and removes numbers. """    
    ports = [int(x) for x in input("Enter ports: ").split()]
    ports = [x for x in ports if x != 0]
    ports = list(set(ports))
    ports.sort()
    ports = list(filter(lambda x: x is not None, ports))
    print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| c |>
I added a line to convert the strings to integers. I hope this helps.
<|/ c |>
<| c |>
I added a line to convert the strings to integers. I hope this helps.
<|/ c |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| c |>
I added a line to convert the strings to integers. I hope this helps.
<|/ c |>
<| a tags=python |>
<code>
def ports_to_ints(ports):
    ports = [int(x) for x in ports]
    return ports
</code>
<|/ a dscore=0 |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| a tags=python |>
<code>
def ports_to_ints(ports):
    ports = [int(x) for x in ports]
    return ports
</code>
<|/ a dscore=0 |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| a dscore=0 tags=python |>
<code>
def ports_to_ints(ports):
    ports = [int(x) for x in ports]
    return ports
</code>
<|/ a |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| c |>
This code works but only if the ports are integers. If the ports are strings it does not work. Is there a way to convert them to integers?
<|/ c |>
<| c |>
This code works but only if the port