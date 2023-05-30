#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and converts a list of words. """    
    port = int(input("Enter a port number: "))
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == 'q':
            break
    
    words = words[:-1]
    
    ports = []
    for word in words:
        ports.append(int(word))
    
    ports.sort()
    
    ports.reverse()
    
    ports.insert(0, port)
    
    ports.reverse()
    
    for port in ports:
        print("Port {} is {}.".format(port, words[port]))
    
