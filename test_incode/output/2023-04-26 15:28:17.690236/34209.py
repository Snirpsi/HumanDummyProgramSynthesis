#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and enumerates a list of words. """    
    while True:
        port = random.randint(10000, 65535)
        words = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        
        word = ''.join(random.choice(words) for _ in range(random.randint(1, 10)))
        
        print('Port {} is {}'.format(port, word))
        
        time.sleep(1)
        
