#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    # Open the file that contains the list of words and read it line by line
    for line in open('words.txt'):
        line = line.strip()
        
        # Add the line to the list of words if it isn't empty
        if line:
            words.append(line)
    
    # Print the list of words back to the user
    print('\n'.join(words))
    
    # Start the webserver
    webserver.run(host='0.0.0.0', port=8080, debug=True)
    
