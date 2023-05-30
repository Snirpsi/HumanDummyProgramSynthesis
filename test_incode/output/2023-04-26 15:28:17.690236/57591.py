#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'monkey', 'horse', 'sheep']
    
    # Iterate over all words and print them
    for word in words:
        print(word)
        
    # Print the length of each word
    for word in words:
        print(len(word))
        
    # Print the longest word
    print(max(words))
    
    # Print the shortest word
    print(min(words))
    
    # Print the average length of the words
    print(sum(words) / len(words))
    
    # Print the average length of the words in reverse order
    print(sum(reversed(words)) / len(words))
    
    # Print the average length of the words in reverse order and print 
    # the number of times each word appears
    print(sum(reversed(words)), len(words))
    
    # Print the average length of the words in reverse order and print 
    # the number of times each word appears ignoring case and punctuation
    print(sum(reversed(words)), len(words), ignorecase=True, punctuation=True)
    
    # Print the average length of the words in reverse order and print 
    # the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation
    print(sum(reversed(words)), len(words), ignorecase=True, punctuation=True, 
          wordcount=True)
    
    # Print the average length of the words in reverse order and print 
    # the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignoring case and punctuation 
    # and print the number of times each word appears ignor