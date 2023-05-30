#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or multiplyes words. """    
    
    ports = input("Enter ports: ")
    words = input("Enter words: ")
    
    ports = ports.split()
    words = words.split()
    
    ports_new = []
    words_new = []
    
    for port in ports:
        if port in ports_new:
            ports_new.remove(port)
        else:
            ports_new.append(port)
    
    for word in words:
        if word in words_new:
            words_new.remove(word)
        else:
            words_new.append(word)
    
    ports_new = list(set(ports_new))
    words_new = list(set(words_new))
    
    ports_new = ''.join(ports_new)
    words_new = ''.join(words_new)
    
    print("Ports: ", ports_new)
    print("Words: ", words_new)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
