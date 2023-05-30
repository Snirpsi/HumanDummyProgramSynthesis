#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or calculates a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if not line:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Store words in list
        words.extend(words)
        
    # Calculate word frequencies
    word_freq = collections.Counter(words)
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('%s: %i' % (word, freq))
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # Print the average word length
    word_freq.most_common(20)
    
    # Print the most common words
    word_freq.most_common(10)
    
    # Print the least common words
    word_freq.most_common()
    
    # 