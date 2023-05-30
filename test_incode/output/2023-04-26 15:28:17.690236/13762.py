#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or converts words. """    
    while True:
        port = random.randint(1, 65535)
        words = input("Enter a word: ")
        words = words.split()
        words = ' '.join(words)
        print(port)
        for word in words:
            print(word, end=' ')
        