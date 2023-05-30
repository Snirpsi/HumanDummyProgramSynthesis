#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Read words from file
    words = []
    with open(args[0], 'r') as file:
        for line in file:
            words.append(line.strip())
    
    # Print list of words
    print('\n'.join(words))
    
    # Print number of words
    print('Number of words: {}'.format(len(words)))
    
    # Print number of vowels
    print('Number of vowels: {}'.format(len([x for x in words if x.isalpha()])))
    
    # Print number of consonants
    print('Number of consonants: {}'.format(len([x for x in words if x.isalpha() and x.islower()])))
    
    # Print number of digits
    print('Number of digits: {}'.format(len([x for x in words if x.isdigit()])))
    
    # Print number of uppercase letters
    print('Number of uppercase letters: {}'.format(len([x for x in words if x.isupper()])))
    
    # Print number of lowercase letters
    print('Number of lowercase letters: {}'.format(len([x for x in words if x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.isupper() and x.islower()])))
    
    # Print number of special characters
    print('Number of special characters: {}'.format(len([x for x in words if x.isalpha() and x.isdigit() and x.