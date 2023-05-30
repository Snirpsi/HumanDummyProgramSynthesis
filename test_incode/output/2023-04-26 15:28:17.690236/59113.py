#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or stores a list of words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        else:
            print(line)
            words.append(line)
    print('The words are:')
    for word in words:
        print(word)
    print('The total words are:', len(words))
    print('The average words are:', sum(words) / len(words))
    print('The worst words are:', words[len(words) // 2])
    print('The least words are:', words[len(words) // 2 - 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 + 1])
    print('The least lengths are:', words[len(words) // 2 - 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 + 1])
    print('The least lengths are:', words[len(words) // 2 - 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The average lengths are:', sum(map(len, words)) / len(words))
    print('The worst lengths are:', words[len(words) // 2 - 1])
    print('The least lengths are:', words[len(words) // 2 + 1])
    print('The 