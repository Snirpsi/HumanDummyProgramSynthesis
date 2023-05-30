#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports or multiplyes words. """    
    ports = input("Enter ports: ")
    words = input("Enter words: ")
    words = words.split()
    ports = ports.split()
    ports_sum = 0
    words_sum = 0
    for port in ports:
        for word in words:
            ports_sum += int(port)
            words_sum += int(word)
    print(ports_sum * words_sum)
