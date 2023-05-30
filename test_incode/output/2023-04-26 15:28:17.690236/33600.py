#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and stores all ports. """    
    
    # read words from file
    words = []
    
    # read all words from file
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
            
    # print all words and ports
    print('\nWords:')
    for word in words:
        print(word)
        print('-' * 20)
    
    # print all ports
    print('\nPorts:')
    for port in range(1, 65535):
        print('\t' + str(port))
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port))
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports
    print('\nWords and ports:')
    for word in words:
        for port in range(1, 65535):
            print('\t' + str(word) + ':' + str(port) + ' (' + str(port) + ')')
        print('-' * 20)
    
    # print all words and ports