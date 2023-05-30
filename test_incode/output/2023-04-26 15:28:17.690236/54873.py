#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words and stores all ports. """    
    words = []
    ports = []
    
    # Read words and ports from stdin
    for line in sys.stdin:
        words = line.split()
        ports = list(map(int, line[:-1].split(',')))
    
    # Print words and ports
    for word in words:
        print(word)
        for port in ports:
            print(port, end=' ')
        print()
    
    # Print all words and ports in sorted order
    for word in sorted(words):
        print(word)
        for port in sorted(ports):
            print(port, end=' ')
        print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=' ')
        print()
    print()
    
    # Print all words and ports in sorted order and print a newline after each
    for word in sorted(words):
        print(word, end=' ')
        for port in sorted(ports):
            print(port, end=