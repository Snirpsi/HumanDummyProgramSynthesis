#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and enumerates words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        words.append(word)
    print('\n'.join(words))
    print('Total words: {}'.format(len(words)))
    print('Total words with punctuation: {}'.format(len([word for word in words if word.isalpha()])))
    print('Total words with numbers: {}'.format(len([word for word in words if word.isdigit()])))
    print('Total words with special characters: {}'.format(len([word for word in words if word.isalnum()])))
    print('Total words with spaces: {}'.format(len([word for word in words if word.isspace()])))
    print('Total words with underscores: {}'.format(len([word for word in words if word.isupper()])))
    print('Total words with hyphens: {}'.format(len([word for word in words if word[0].isdigit()])))
    print('Total words with apostrophes: {}'.format(len([word for word in words if word[-1].isdigit()])))
    print('Total words with quotes: {}'.format(len([word for word in words if word[0]=='\'' and word[-1]=='\''])))
    print('Total words with apostrophes and quotes: {}'.format(len([word for word in words if word[0]=='\'' and word[-1]=='\'' and word[1:-1]=='\''])))
    print('Total words with apostrophes and apostrophes: {}'.format(len([word for word in words if word[0]=='\'' and word[-1]=='\'' and word[1:-1]=='\'' and word[1:-1][1:-1]=='\''])))
    print('Total words with apostrophes and apostrophes and apostrophes: {}'.format(len([word for word in words if word[0]=='\'' and word[-1]=='\'' and word[1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1][1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]=='\'' and word[1:-1]