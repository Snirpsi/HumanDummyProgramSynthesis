#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words and adds words. """    
    words = []
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split into words
        words = line.split(' ')
        
        # Print the word list
        print(' '.join(words))
        
    # Print the word list
    print(' '.join(words))
    
    # Calculate and print the word count
    word_count = sum(len(word) for word in words)
    print('Number of words: {}'.format(word_count))
    
    # Calculate and print the word frequency
    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    print('Number of times a word appears: {}'.format(len(word_frequency)))
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_count
    print('Word frequency distribution:')
    print(word_frequency_distribution)
    
    # Calculate and print the word frequency distribution
    word_frequency_distribution = {}
    for word in word_frequency:
        word_frequency_distribution[word] = word_frequency[word] / word_