#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    ports = enumerate()
    for port in ports:
        print(port)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am not allowed to use any external libraries. I just need to run this script from my terminal. Can you please tell me how to do that?
<|/ c |>
<| c |>
I added a script that you can run in your terminal. Hope that helps.
<|/ c |>
<| c |>
Thanks again. Can you please tell me how to run this script from my terminal? I am not familiar with terminal so please explain in detail.
<|/ c |>
<| c |>
I added a script that you can run in your terminal. Hope that helps.
<|/ c |>
<| c |>
Thanks again. Can you please tell me how to run this script from my terminal? I am not familiar with terminal so please explain in detail.
<|/ c |>
<| a tags=python,python-3.x |>
This should work:
<code>
import serial
import sys

ports = [
    port for port in serial.tools.list_ports.comports()
    if port.manufacturer == "Microchip" and port.product == "MSP430"
]
for port in ports:
    print(port)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am not allowed to use any external libraries. I just need to run this script from my terminal. Can you please tell me how to do that?
<|/ c |>
<| c |>
I added a script that you can run in your terminal. Hope that helps.
<|/ c |>
<| c |>
Thanks again. Can you please tell me how to run this script from my terminal? I am not familiar with terminal so please explain in detail.
<|/ c |>
<| c |>
I added a script that you can run in your terminal. Hope that helps.
<|/ c |>
<| c |>
Thanks again. Can you please tell me how to run this script from my terminal? I am not familiar with terminal so please explain in detail.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
import serial
import sys

ports = [
    port for port in serial.tools.list_ports.comports()
    if port.manufacturer == "Microchip" and port.product == "MSP430"
]
