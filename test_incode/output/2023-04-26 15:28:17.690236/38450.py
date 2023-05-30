#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and enumerates user input. """    
    words = []
    word = None
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
    
    for word in words:
        print(word)
    
    print("\nEnter a number: ")
    
    while True:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        if number < 0 or number > len(words):
            print("Invalid number")
            continue
        
        print(words[number])
    
    print("\nEnter a letter: ")
    
    while True:
        letter = input("Enter a letter: ")
        
        if letter == "":
            break
        
        if letter not in word:
            print("Invalid letter")
            continue
        
        print(letter)
    
    print("\nEnter a word: ")
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        if word not in words:
            print("Invalid word")
            continue
        
        print(word)
    
    print("\nEnter a number: ")
    
    while True:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        if number < 0 or number > len(words):
            print("Invalid number")
            continue
        
        print(words[number])
    
    print("\nEnter a letter: ")
    
    while True:
        letter = input("Enter a letter: ")
        
        if letter == "":
            break
        
        if letter not in word:
            print("Invalid letter")
            continue
        
        print(letter)
    
    print("\nEnter a word: ")
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        if word not in words:
            print("Invalid word")
            continue
        
        print(word)
    
    print("\nEnter a number: ")
    
    while True:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        if number < 0 or number > len(words):
            print("Invalid number")
            continue
        
        print(words[number])
    
    print("\nEnter a letter: ")
    
    while True:
        letter = input("Enter a letter: ")
        
        if letter == "":
            break
        
        if letter not in word:
            print("Invalid letter")
            continue
        
        print(letter)
    
    print("\nEnter a word: ")
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        if word not in words:
            print("