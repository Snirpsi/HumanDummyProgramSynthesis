#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens words.txt and reads it
    wordlist = open("words.txt","r")
    wordlist = wordlist.read()
    wordlist = wordlist.split()
    #A function that prints all the words in the file
    for word in words:
        print(word)
    #A function that prints the words in the file that start with a vowel
    for word in words:
        if word[0] in "aeiou":
            print(word)
    #A function that prints the words in the file that start with a consonant
    for word in words:
        if word[0] in "bcdfghjklmnpqrstvwxyz":
            print(word)
    #A function that prints the words in the file that start with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        if word[4] in "aeiou":
                            print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        if word[4] in "aeiou":
                            if word[5] in "bcdfghjklmnpqrstvwxyz":
                                print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        if word[4] in "aeiou":
                            if word[5] in "bcdfghjklmnpqrstvwxyz":
                                if word[6] in "aeiou":
                                    print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        if word[4] in "aeiou":
                            if word[5] in "bcdfghjklmnpqrstvwxyz":
                                if word[6] in "aeiou":
                                    if word[7] in "bcdfghjklmnpqrstvwxyz":
                                        print(word)
    #A function that prints the words in the file that start with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant and ends with a vowel and a consonant
    for word in words:
        if word[0] in "aeiou":
            if word[1] in "bcdfghjklmnpqrstvwxyz":
                if word[2] in "aeiou":
                    if word[3] in "bcdfghjklmnpqrstvwxyz":
                        if word[4] in "aeiou":
                            if word[5] in "bcdfghjklmnpqrstvwxyz":
                                if word[6] in "aeiou":
                                    if word[7] in "bcdfghjk

