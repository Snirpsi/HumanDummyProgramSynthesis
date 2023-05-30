#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    #The function takes a list of words and returns a list of tuples containing the word and the number of occurrences.
    #The function also prints the number of occurrences for each word.
    words = [w.lower() for w in words]
    word_counts = collections.Counter(words)
    for word, count in word_counts.items():
        print(word, count)
    print("Number of occurrences of each word:")
    for word, count in word_counts.items():
        print(word, count)

