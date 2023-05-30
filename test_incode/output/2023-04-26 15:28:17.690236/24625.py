#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and opens fruits. """    
    while True:
        port = random.randint(10000, 20000)
        fruit = Fruit(port)
        fruit.open()
        time.sleep(2)
