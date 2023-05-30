#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and adds words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words = add_words(words)
    
    with open('words.txt', 'w') as file:
        for line in words:
            file.write(line + '\n')
    
