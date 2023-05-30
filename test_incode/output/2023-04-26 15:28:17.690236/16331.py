#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and stores all ports. """    
    
    # Load words from file
    words = []
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Add words to dictionary
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict[word] + 1
    
    # Add ports to dictionary
    ports_dict = {}
    for port in range(1, 65535):
        ports_dict[port] = ports_dict[port] + 1
    
    # Print dictionary
    print('Dictionary of words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    for key, value in ports_dict.items():
        print('{}: {}'.format(key, value))
    print('')
    
    # Print all words and ports
    print('All words and ports:')
    for key, value in words_dict.items():
        print('{}: {}'.format(key, 