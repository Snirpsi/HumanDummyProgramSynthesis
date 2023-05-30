#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or adds a list of words. """    
    port = 0
    words = []
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        else:
            port = int(port)
            words.append(port)
    
    words.sort()
    
    for word in words:
        print(word, end=' ')
    
