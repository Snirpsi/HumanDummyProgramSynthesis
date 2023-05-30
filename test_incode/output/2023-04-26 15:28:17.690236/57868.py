#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and opens words. """    
    numbers = range(1,10)
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for number in numbers:
        print(number)
        for word in words:
            if number == word:
                print(word)
                break
            else:
                print("