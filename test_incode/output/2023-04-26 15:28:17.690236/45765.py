#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and returns words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Store words in global variable
    words = words
    
    # Return words in JSON format
    return jsonify(words)
