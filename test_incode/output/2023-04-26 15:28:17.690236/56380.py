#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    # Read in words from file
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    # Calculate list of words
    words = calculate_words(words)
    
    # Print list of words
    print(words)
    
    # Write list of words to file
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
    
