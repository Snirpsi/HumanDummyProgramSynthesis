#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and opens words. """    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    with open('words.txt', 'w') as file:
        for word in words:
            file.write(word + '\n')
    
