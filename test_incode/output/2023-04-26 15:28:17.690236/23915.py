#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or prints a list of words. """    
    words = []
    
    # Open words and print them if they exist.
    for line in open('words.txt'):
        line = line.strip()
        if line:
            words.append(line)
    
    # Print all words if they exist.
    if words:
        print('\n'.join(words))
    else:
        print('No words found.')
    
