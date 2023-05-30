#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates words.
    #The enumerate function returns a generator that yields tuples of words.
    #The tuple is (word, index) where index is the index of the word in the list.
    #The generator is then consumed by for loop to print each word.
    #The for loop iterates over the generator and prints each word.
    for word in enumerate(words):
        print(word[0], word[1])

