#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or enumerates a list of words. """    
    
    ports = input("Enter the ports separated by commas: ")
    words = input("Enter the words separated by commas: ")
    
    words = words.split(',')
    ports = ports.split(',')
    
    ports = list(set(ports))
    words = list(set(words))
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    ports_set.difference_update(words_set)
    
    ports = list(ports_set)
    words = list(words_set)
    
    ports.sort()
    words.sort()
    
    ports_set = set(ports)
    words_set = set(words)
    
    