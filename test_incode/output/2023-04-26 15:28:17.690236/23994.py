#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        word = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(1, 10)))
        
        