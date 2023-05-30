#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and converts words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('The total word count is:', len(words))
    print('The average word count is:', sum(words) / len(words))
    print('The longest word is:', max(words))
    print('The shortest word is:', min(words))
    print('The most common word is:', words[0])
    print('The least common word is:', words[-1])
    print('The word with the lowest frequency is:', words.count(words[0]))
    print('The word with the highest frequency is:', words.count(words[-1]))
    print('The word with the most common letter is:', words[words.count(words[0])])
    print('The word with the least common letter is:', words[words.count(words[-1])])
    print('The word with the most common number is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common number is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common symbol is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common symbol is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common punctuation is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common punctuation is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common question mark is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common question mark is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common exclamation mark is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common exclamation mark is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common question mark is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common question mark is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common exclamation mark is:', words[words.count(words[words.count(words[0])])])
    print('The word with the least common exclamation mark is:', words[words.count(words[words.count(words[-1])])])
    print('The word with the most common question mark 