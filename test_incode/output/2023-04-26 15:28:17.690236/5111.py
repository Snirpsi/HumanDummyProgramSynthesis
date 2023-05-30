#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers or iterates over a list of words. """    
    
    # Read in words from a file
    words = []
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Iterate over words and add them to dictionary
    word_dict = dict()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    
    # Print the word counts
    for word, count in word_dict.items():
        print(word, count)
    
    # Print the word counts sorted by most common word
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] + count
        else:
            word_dict[word] = count
    
    # Print the word counts sorted by least common word
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] - count
        else:
            word_dict[word] = count
    
    # Print the word counts sorted by most common word with negative values
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] + -count
        else:
            word_dict[word] = -count
    
    # Print the word counts sorted by least common word with negative values
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] - -count
        else:
            word_dict[word] = -count
    
    # Print the word counts sorted by most common word with positive values
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] + count
        else:
            word_dict[word] = count
    
    # Print the word counts sorted by least common word with positive values
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] - count
        else:
            word_dict[word] = count
    
    # Print the word counts sorted by most common word with positive values 
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = word_dict[word] + -count
        else:
            word_dict[word] = -count
    
    # Print the word counts sorted by least common word with positive values 
    word_dict = dict()
    for word, count in word_dict.items():
        if word in word_dict:
            word_dict[word] = 