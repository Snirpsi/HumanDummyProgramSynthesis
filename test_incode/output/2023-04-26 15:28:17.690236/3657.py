#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and returns a list of numbers. """    
    ports = []
    while True:
        ports.append(randint(1,65535))
        print(ports)
        time.sleep(1)
</code>
<|/ a tags=python,python-3.x,while-loop,infinite-loop |>
<| a dscore=0 |>
I believe this should work:
<code>
import time
from random import randint

while True:
    ports = [randint(1,65535) for _ in range(10)]
    print(ports)
    time.sleep(1)
</code>
<|/ a tags=python,python-3.x,while-loop,infinite-loop |>
<| c |>
This would only print 10 random numbers, not 10 numbers between 1 and 65535.
<|/ c |>
<| c |>
I believe it does, I tested it and it does print 10 random numbers between 1 and 65535
<|/ c |>
<| c |>
It does print 10 numbers between 1 and 65535, but only 10 numbers between 1 and 65535. 