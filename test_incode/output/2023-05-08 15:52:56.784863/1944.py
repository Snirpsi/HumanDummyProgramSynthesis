#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that converts words.
    #It takes a list of words and converts them into sentences.
    #It returns a list of sentences.
    #The function uses list comprehension to convert each word into sentence.
    sentences = [" ".join(word) for word in words]
    print(sentences)

