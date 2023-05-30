#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and returns all ports. """    
    words = ['word1', 'word2']
    ports = []
    while True:
        ports.append(random.choice(words))
        