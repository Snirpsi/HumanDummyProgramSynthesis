#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and calculates all ports. """    
    words = ['word1', 'word2', 'word3']
    ports = []
    for word in words:
        ports.append(len(word))
    
    ports = list(set(ports))
    
    ports.sort(reverse=True)
    
    for port in ports:
        print(port