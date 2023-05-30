#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and removes all ports. """    
    ports = input("Enter the ports separated by spaces (no spaces!): ")
    ports = ports.split()
    ports = [int(port) for port in ports]
    ports = [port for port in ports if port > 0]
    ports = [port for port in ports if port < 65535]
    ports = [port for port in ports if port > 65535]
    ports = [port for port in ports if port != 0]
    ports = [port for port in ports if port != 65535]
    ports.sort()
    print(ports)
</code>
<|/ a |>
<| c |>
Thank you very much! It works perfectly! I really appreciate your help!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| a dscore=0 tags=python,python-3.x,python-2.7 |>
<code>
ports = [port for port in ports if port > 65535]
</code>
This line is wrong. You are trying to compare a number to a list. Try this:
<code>
ports = [port for port in ports if port > 65535]
</code>
<|/ a |>
<| c |>
Thank you very much! It works perfectly! I really appreciate your help!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| a tags=python,python-3.x,python-2.7 |>
<code>
ports = [port for port in ports if port > 65535]
</code>
This line is wrong. You are trying to compare a number to a list. Try this:
<code>
ports = [port for port in ports if port > 65535]
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! It works perfectly! I really appreciate your help!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| a dscore=0 |>
<code>
ports = [port for port in ports if port > 65535]
</code>
This line is wrong. You are trying to compare a number to a list. Try this:
<code>
ports = [port for port in ports if port > 65535]
</code>
<|/ a tags=python,python-3.x,python-2.7 |>
<| c |>
Thank you very much! It works perfectly! I really appreciate your help!
