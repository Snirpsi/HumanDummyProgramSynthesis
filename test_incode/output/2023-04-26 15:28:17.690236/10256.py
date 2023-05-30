#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Open the file that contains the words to enumerate.
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the words in the file.
    for word in words:
        print(word)
        
    # Start the webserver.
    webserver.run(host='0.0.0.0', port=8080)
    
    # 