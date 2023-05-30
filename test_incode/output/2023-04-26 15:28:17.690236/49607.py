#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and iterates over a list of words. """    
    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    ports = []
    for word in words:
        ports.append(get_port(word))
    
    print('\n'.join(ports))

<|/ file ext=.py |>