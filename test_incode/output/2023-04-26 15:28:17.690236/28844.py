#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or converts words. """    
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
    print('The total is', len(words))
    print('The average is', sum(words) / len(words))
    print('The highest is', max(words))
    print('The lowest is', min(words))
    print('The average is', sum(words) / len(words))
    print('The word with the highest frequency is', max(words))
    print('The word with the lowest frequency is', min(words))
    print('The word with the highest frequency and lowest frequency is', max(words), min(words))
    print('The word with the highest frequency and lowest frequency and their frequency is', max(words), min(words), sum(words) / len(words))
    print('The word with the highest frequency and lowest frequency and their frequency and their frequency is', max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(words) / len(words), max(words), min(words), sum(