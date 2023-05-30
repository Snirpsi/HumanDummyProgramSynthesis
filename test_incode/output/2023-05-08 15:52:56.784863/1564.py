#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that calculates words.
    #It takes two arguments: one is the text to calculate and the other is the words to calculate
    #It then prints the word count of the text in the first argument and the word count of the text in the second argument.
    #The program is called from the command line.
    import sys
    wordcount1 = len(sys.argv[1])
    wordcount2 = len(sys.argv[2])
    print(wordcount1, wordcount2)

