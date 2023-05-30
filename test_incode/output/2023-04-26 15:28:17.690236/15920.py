#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Get the word list
    word_list = args.pop(0)
    
    # Get the word count
    word_count = len(word_list)
    
    # Get the word frequency
    word_frequency = {}
    
    # Loop over the word list
    for word in word_list:
        
        # Check if word is in dictionary
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    # Get the word frequency
    word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the word frequency
    print('\n'.join(['%s: %s' % (word, freq) for word, freq in word_frequency]))
    
