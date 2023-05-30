#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    
    # Read in all words from file
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    # Remove all words that start with a vowel
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = [word for word in words if word[0] in vowels]
    
    # Write to file
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
            
    print('Done!')
    
