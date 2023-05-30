#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words or stores user input. """    
    
    # Read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    # Print the list of words
    print('\n'.join(words))
    
    # Calculate and print the average of the words in the list
    average = sum(words) / len(words)
    print('The average of the words is {}'.format(average))
    
    # Calculate and print the median of the words in the list
    median = sorted(words)[len(words) / 2]
    print('The median of the words is {}'.format(median))
    
    # Calculate and print the mode of the words in the list
    mode = sorted(words)[0]
    print('The mode of the words is {}'.format(mode))
    
    # Calculate and print the frequency of the words in the list
    freq = Counter(words)
    print('The frequency of the words is {}'.format(freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
    
    # Calculate and print the frequency of the words in the list
    freq = freq.most_common()
    print('The most common words are:')
    for word, freq in freq:
        print('{}: {}'.format(word, freq))
