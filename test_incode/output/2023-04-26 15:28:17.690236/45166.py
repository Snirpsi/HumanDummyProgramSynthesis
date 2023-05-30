#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    
    # Load words from file
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Remove words
    removed = []
    for word in words:
        if word not in removed:
            removed.append(word)
    
    # Write to file
    with open('words.txt', 'w') as f:
        for line in removed:
            f.write(line)
            f.write('\n')
    
