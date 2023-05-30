#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and opens fruits. """    
    while True:
        words = input("Enter a word: ")
        if words.isalpha():
            words = words.split()
            fruits = open("fruits.txt", "w")
            for word in words:
                fruits.write(word + "\n")
            fruits.close()
        else:
            print("Invalid input")
