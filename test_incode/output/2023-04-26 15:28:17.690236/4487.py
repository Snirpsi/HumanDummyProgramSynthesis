#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
            
    # Print words to screen
    print('Words: {}'.format(words))
    
    # Store words to file
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
    
    # Close file
    file.close()
    
    # Print number of words stored
    print('Number of words: {}'.format(len(words)))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines())))
    
    # Print number of words in file
    print('Number of words in file: {}'.format(len(open('words.txt').readlines()