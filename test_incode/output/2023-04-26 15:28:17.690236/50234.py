#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and calculates fruits. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        words.append(line)
    
    # Calculate fruits
    fruits = calculate_fruits(words)
    
    # Print the results
    for fruit in fruits:
        print('{}: {}'.format(*fruit))
    
    # Print the server address
    print('Serving on http://{}:{}/'.format(*