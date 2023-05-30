#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and opens fruits. """    
    
    words = []
    
    # Open the fruits file
    with open('fruits.txt', 'r') as fruits:
        for line in fruits:
            line = line.strip()
            if line != '':
                words.append(line)
    
    # Open the words file
    with open('words.txt', 'r') as words:
        for line in words:
            line = line.strip()
            if line != '':
                words.append(line)
    
    # Print the list of words
    print(words)
    
    # Open the fruits file
    with open('fruits.txt', 'w') as fruits:
        for line in words:
            fruits.write(line + '\n')
    
    # Open the words file
    with open('words.txt', 'w') as words:
        for line in words:
            words.write(line + '\n')
    
    # Print the list of words
    print(words)
    
    # Close the fruits file
    with open('fruits.txt', 'w') as fruits:
        fruits.close()
    
    # Close the words file
    with open('words.txt', 'w') as words:
        words.close()
    
    # Close the web server
    server.socket.close()
    
    # Close the Python interpreter
    