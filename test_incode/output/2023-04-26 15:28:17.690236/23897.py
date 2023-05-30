#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over fruits or iterates over a list of words. """    
    
    # Iterate over fruits
    for fruit in fruits:
        print(fruit)
    
    # Iterate over words
    for word in words:
        print(word)
    
    # Iterate over list of words
    for word in words:
        for fruit in fruits:
            print(word, fruit)
    
    # Iterate over list of fruits
    for fruit in fruits:
        for word in words:
            print(word, fruit)
    
    # Iterate over list of words and fruits
    for word in words:
        for fruit in fruits:
            print(word, fruit)
    
    # Iterate over list of words and fruits using zip
    for word in words:
        for fruit in fruits:
            print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate
    for word, fruit in zip(words, fruits):
        print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip
    for word, fruit in zip(words, fruits):
        for index, letter in enumerate(word):
            print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip and enumerate
    for word, fruit in zip(words, fruits):
        for index, letter in enumerate(word):
            for index, letter2 in enumerate(word):
                print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip and enumerate and zip
    for word, fruit in zip(words, fruits):
        for index, letter in enumerate(word):
            for index, letter2 in enumerate(word):
                for index, letter3 in enumerate(word):
                    print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip and enumerate and zip and enumerate
    for word, fruit in zip(words, fruits):
        for index, letter in enumerate(word):
            for index, letter2 in enumerate(word):
                for index, letter3 in enumerate(word):
                    for index, letter4 in enumerate(word):
                        for index, letter5 in enumerate(word):
                            print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip and enumerate and zip and enumerate and zip
    for word, fruit in zip(words, fruits):
        for index, letter in enumerate(word):
            for index, letter2 in enumerate(word):
                for index, letter3 in enumerate(word):
                    for index, letter4 in enumerate(word):
                        for index, letter5 in enumerate(word):
                            for index, letter6 in enumerate(word):
                                print(word, fruit)
    
    # Iterate over list of words and fruits using zip and enumerate and zip and enumerate and zip and enumerate and zip and enumerate and 