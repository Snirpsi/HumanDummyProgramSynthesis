#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    # Read in the words from the file
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    # Print the words to the screen
    print('\n'.join(words))
    
    # Start the server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start the server
    server.serve_forever()

<|/ file filename=wordlist.py source=github |>