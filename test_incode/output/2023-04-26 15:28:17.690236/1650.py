#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and iterates over words. """    
    port = 0
    while True:
        port = port + 1
        word = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(3, 10)))
        print('Port', port, '-', word)
        time.sleep(1)
        
