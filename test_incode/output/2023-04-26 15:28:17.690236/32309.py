#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and adds numbers. """    
    words = open("words.txt").read().splitlines()
    numbers = open("numbers.txt").read().splitlines()
    
    for word in words:
        number = numbers[words.index(word)]
        
        words[words.index(word)] = str(number)+word
        
    with open("words.txt", "w") as f:
        f.writelines(words)
        
    with open("numbers.txt", "w") as f:
        f.writelines(numbers)
    
