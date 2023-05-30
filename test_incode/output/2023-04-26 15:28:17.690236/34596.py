#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and removes user input. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
        
    # Remove user input
    words = [word for word in words if word != '']
    
    # Print the results
    for word in words:
        print(word)
        
    # 