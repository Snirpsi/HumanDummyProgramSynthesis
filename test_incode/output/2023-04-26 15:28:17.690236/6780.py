#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and adds all ports. """    
    while True:
        words = ['word1', 'word2']
        ports = [8080, 8081]
        
        for word in words:
            ports.append(random.randint(