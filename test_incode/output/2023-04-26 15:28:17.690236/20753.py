#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Loop over the words and print them
    for word in words:
        print(word)
        
    # Print the length of each word
    print('Length of each word:')
    for word in words:
        print(len(word))
        
    # Print the longest word
    print('Longest word:')
    print(max(words))
    
    # Print the shortest word
    print('Shortest word:')
    print(min(words))
    
    # Print the average length of the words
    print('Average length of words:')
    print(sum(words) / len(words))
    
    # Print the average length of the words in reverse order
    print('Average length of words in reverse order:')
    print(sum(reversed(words)) / len(words))
    
    # Print the average length of the words in reverse order and print a newline
    print('Average length of words in reverse order and print a newline:')
    print(sum(reversed(words)) / len(words) + 