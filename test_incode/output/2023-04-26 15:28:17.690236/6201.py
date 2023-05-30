#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and enumerates a list of words. """    
    words = ["cat", "dog", "bird"]
    numbers = [1, 2, 3, 4, 5]
    
    words.sort()
    numbers.sort()
    
    print("The words are:")
    for word in words:
        print(word)
    
    print("The numbers are:")
    for number in numbers:
        print(number)
    
    print("The words are in alphabetical order:")
    for index, word in enumerate(words):
        print(word, "is", words[index])
    
    print("The numbers are in numerical order:")
    for index, number in enumerate(numbers):
        print(number, "is", numbers[index])
    
    print("The words are in reverse alphabetical order:")
    for index, word in enumerate(reversed(words)):
        print(word, "is", words[index])
    
    print("The numbers are in reverse numerical order:")
    for index, number in enumerate(reversed(numbers)):
        print(number, "is", numbers[index])
    
    print("The words are in alphabetical order and in numerical order:")
    for index, word in enumerate(words):
        print(word, "is", words[index], "and", numbers[index])
    
    print("The numbers are in alphabetical order and in numerical order:")
    for index, number in enumerate(numbers):
        print(number, "is", numbers[index], "and", numbers[index])
    
    print("The words are in alphabetical order and in numerical order and in reverse numerical order:")
    for index, word in enumerate(reversed(words)):
        print(word, "is", words[index], "and", numbers[index], "and", numbers[index])
    
    print("The numbers are in alphabetical order and in numerical order and in reverse numerical order:")
    for index, number in enumerate(reversed(numbers)):
        print(number, "is", numbers[index], "and", numbers[index], "and", numbers[index])
    
    print("The words are in alphabetical order and in numerical order and in reverse numerical order and in reverse alphabetical order:")
    for index, word in enumerate(reversed(words)):
        print(word, "is", words[index], "and", numbers[index], "and", numbers[index], "and", numbers[index])
    
    print("The numbers are in alphabetical order and in numerical order and in reverse numerical order and in reverse alphabetical order:")
    for index, number in enumerate(reversed(numbers)):
        print(number, "is", numbers[index], "and", numbers[index], "and", numbers[index], "and", numbers[index])
    
    print("The words are in alphabetical order and in numerical order and in reverse numerical order and in reverse alphabetical order and in reverse alphabetical order:")
    for index, word in 