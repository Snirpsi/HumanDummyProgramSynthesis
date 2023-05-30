#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and removes a list of words. """    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    words = words.split()
    numbers = numbers.split()
    
    numbers_clean = []
    words_clean = []
    
    for number in numbers:
        if number not in numbers_clean:
            numbers_clean.append(number)
    for word in words:
        if word not in words_clean:
            words_clean.append(word)
    
    print("Numbers cleaned:", numbers_clean)
    print("Words cleaned:", words_clean)
    
