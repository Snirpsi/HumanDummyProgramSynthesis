#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or adds a port. """    
    port = '8080'
    
    words = []
    
    # Read all words from file
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Add port to each word
    for word in words:
        word = '{}:{}'.format(word, port)
        
        print(word)
        
    # Print the whole list
    print(words)
    
    # Print the port number for each word
    for word in words:
        print(word, ":", words.index(word) + 1)
        
    # Print the port number for each word with its position
    for word, position in zip(words, range(len(words))):
        print(word, ":", position + 1)
        
    # Print the port number for each word with its position and its word
    for word, position, word in zip(words, range(len(words)), words):
        print(word, ":", position + 1, word)
        
    # Print the port number for each word with its position and its word and port
    for word, position, word, port in zip(words, range(len(words)), words, range(port)):
        print(word, ":", position + 1, word, ":", port)
        
    # Print the port number for each word with its position and its word and port and port
    for word, position, word, port, port in zip(words, range(len(words)), words, range(port), range(port)):
        print(word, ":", position + 1, word, ":", port, ":", port)
        
    # Print the port number for each word with its position and its word and port and port and port
    for word, position, word, port, port, port in zip(words, range(len(words)), words, range(port), range(port), range(port)):
        print(word, ":", position + 1, word, ":", port, ":", port, ":", port)
        
    # Print the port number for each word with its position and its word and port and port and port and port
    for word, position, word, port, port, port, port in zip(words, range(len(words)), words, range(port), range(port), range(port), range(port), range(port)):
        print(word, ":", position + 1, word, ":", port, ":", port, ":", port, ":", port)
        
    # Print the port number for each word with its position and its word and port and port and port and port and port
    for word, position, word, port, port, port, port, port in zip(words, range(len(words)), words, range(port), range(port), range(port), range(port), range(port), range(port), range(port)):
        print(word, ":", position + 1, word, ":", port, ":", port, ":", port, ":", port, ":", port)
        
    # Print the port number for each word with its position and its word and port and port and port and port and port 