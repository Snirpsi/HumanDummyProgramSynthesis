#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4']
    
    # Create a list to hold the result
    word_list = []
    
    # Iterate through the words and add them to the list
    for word in words:
        word_list.append(word)
    
    # Print the list
    print(word_list)
    
    # Print the length of the list
    print(len(word_list))
    
    # Print the average length of the list
    print(sum(word_list) / len(word_list))
    
    # Print the average length of the list ignoring duplicates
    print(sum(word_list) / len(word_list) - len(set(word_list)))
    
    # Print the average length of the list ignoring duplicates and ignoring duplicates
    print(sum(word_list) / len(word_list) - len(set(word_list)) 