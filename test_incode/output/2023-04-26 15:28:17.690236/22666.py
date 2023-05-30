#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and prints all ports. """    
    while True:
        word = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(1,10)))
        ports = ports_for_key(word)
        for port in ports:
            print(port, end=' ')
        print()
        time.sleep(1)
