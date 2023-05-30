#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and multiplyes fruits. """    
    ports = [
        port for port in os.listdir('/dev/ttyUSB')
        if port.startswith('ttyUSB') and port.isdigit()
    ]
    fruits = [
        port * 3 for port in ports
    ]
    print(fruits)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help! I really appreciate it!
<|/ c |>
<| c |>
No problem, glad I could help.
<|/ c |>
<| a tags=python,raspberry-pi,python-3.x |>
<code>
import serial

ports = [
    port for port in os.listdir('/dev/ttyUSB')
    if port.startswith('ttyUSB') and port.isdigit()
]
fruits = [
    port * 3 for port in ports
]
print(fruits)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help! I really appreciate it!
<|/ c |>
<| c |>
No problem, glad I could help.
<|/ c |>
<| c |>
Thanks so much for your help! I really appreciate it!
<|/ c |>
<| c |>
No problem, glad I could help.
<|/ c |>