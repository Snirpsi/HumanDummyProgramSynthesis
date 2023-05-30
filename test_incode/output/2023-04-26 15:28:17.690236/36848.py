#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
            
    # Store words in dictionary
    words_dict = dict(zip(words, range(len(words))))
    
    # Print words in dictionary
    for word in words:
        print(word, words_dict[word])
        
    # Print the longest word
    print(max(words_dict.values()))
    
    # Print the shortest word
    print(min(words_dict.values()))
    
    # Print the average of the longest and shortest words
    print(sum(words_dict.values()) / len(words_dict))
    
    # Print the average of the longest and shortest words with spaces
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(min(words_dict.values()), end=' ')
    print(max(words_dict.values()), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    
    # Print the average of the longest and shortest words with spaces and punctuation
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(min(words_dict.values()), end=' ')
    print(max(words_dict.values()), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    
    # Print the average of the longest and shortest words with spaces and punctuation
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(min(words_dict.values()), end=' ')
    print(max(words_dict.values()), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    
    # Print the average of the longest and shortest words with spaces and punctuation
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(min(words_dict.values()), end=' ')
    print(max(words_dict.values()), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    print(sum(words_dict.values()) / len(words_dict), end=' ')
    
    # Print the average of the longest and shortest words with spaces and punctuation
    print(sum(words_dict.values()) / len(words_dict), 