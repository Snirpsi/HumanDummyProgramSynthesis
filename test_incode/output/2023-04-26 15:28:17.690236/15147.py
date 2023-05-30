#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    # Read in text from file
    with open('./input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    # Calculate word frequencies
    word_freq = Counter(words)
    
    # Print word frequencies
    for word, freq in word_freq.items():
        print('{}: {}'.format(word, freq))
    
    # Print the most common word
    print('Most common word:')
    print(word_freq.most_common(1)[0][0])
    
    # Print the least common word
    print('Least common word:')
    print(word_freq.most_common(1)[0][1])
    
    # Print the average word frequency
    print('Average word frequency:')
    print(word_freq.most_common(1)[0][2])
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
    
    # Print the word count
    print('Word count:')
    print(len(word_freq))
