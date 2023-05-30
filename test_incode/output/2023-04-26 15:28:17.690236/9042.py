#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = []
    
    # Open the file containing the words and parse them
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            # If the line starts with '#', ignore it
            if line.startswith('#'):
                continue
            
            # If the line is empty, ignore it
            if line == '':
                continue
            
            # Otherwise, add the line to the list of words
            else:
                words.append(line)
                
    # Print the list of words to the screen
    print('\n'.join(words))
    
    # Start the webserver
    webserver.serve_forever()

<|/ file filename=wordlist.py ext=.py |>