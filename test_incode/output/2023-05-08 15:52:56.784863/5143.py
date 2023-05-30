#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    #It then prints them out in alphabetical order.
    #It then asks the user if they want to quit or continue to work.
    wordlist = list(set(words))
    wordlist.sort()
    print(wordlist)
    wordlist = input("Would you like to quit or continue to work? ")
    if wordlist == "quit":
        print("Goodbye!")
        exit()
    elif wordlist == "continue":
        print("Continuing to work...")
    else:
        print("Invalid input.")

