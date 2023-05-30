#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Open the file containing words and add them to the list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Print the list of words to the user
    print('\n'.join(words))
    
    # Start the webserver
    webserver.run(host='0.0.0.0', port=8080)
    
    # 