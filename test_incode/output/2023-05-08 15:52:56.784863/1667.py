#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that removes words.
    def remove_words(words):
        words = [word for word in words if word not in words]
        return words
    words = remove_words(words)
    print(words)

