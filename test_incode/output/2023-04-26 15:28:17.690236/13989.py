#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and calculates words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Calculate words' frequencies
    word_frequencies = {}
    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    
    # Print the results
    for word, frequency in word_frequencies.items():
        print('{}: {}'.format(word, frequency))
    
    # Print the sorted results
    for word, frequency in sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True):
        print('{}: {}'.format(word, frequency))
    
    # Print the most common word
    print('Most common word:')
    most_common_word = max(word_frequencies.items(), key=lambda x: x[1])[0]
    print('{}: {}'.format(most_common_word, word_frequencies[most_common_word]))
    
    # Print the least common word
    print('Least common word:')
    least_common_word = min(word_frequencies.items(), key=lambda x: x[1])[0]
    print('{}: {}'.format(least_common_word, word_frequencies[least_common_word]))
    
    # Print the most common words' frequencies
    print('Most common words and their frequencies:')
    for word, frequency in word_frequencies.items():
        print('{}: {}'.format(word, frequency))
    
    # Print the least common words' frequencies
    print('Least common words and their frequencies:')
    for word, frequency in word_frequencies.items():
        print('{}: {}'.format(word, frequency))
    
    # Print the most common words' frequencies and their frequencies
    print('Most common words and their frequencies and their frequencies:')
    for word, frequency in word_frequencies.items():
        print('{}: {} and {}'.format(word, frequency, word_frequencies[word]))
    
    # Print the least common words and their frequencies and their frequencies
    print('Least common words and their frequencies and their frequencies:')
    for word, frequency in word_frequencies.items():
        print('{}: {} and {}'.format(word, frequency, word_frequencies[word]))
    
    # Print the most common words and their frequencies and their frequencies and their frequencies
    print('Least common words and their frequencies and their frequencies and their frequencies:')
    for word, frequency in word_frequencies.items():
        print('{}: {} and {} and {}'.format(word, frequency, word_frequencies[word], word_frequencies[least_common_word]))
    
    # Print the most common words and their frequencies and their frequencies and their frequencies
    print('Least common words and their frequencies and their frequenci