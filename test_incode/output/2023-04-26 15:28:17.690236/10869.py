#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or removes fruits. """    
    while True:
        ports = list(fruits.keys())
        fruits.pop(random.choice(ports))
        print(ports)
        time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! I 