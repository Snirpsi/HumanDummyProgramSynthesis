#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that requests words.
    #It then prints them out in reverse order.
    #It then asks the user if they want to quit.
    words = list(input("Enter words: ").split())
    words.reverse()
    print(" ".join(words))
    quit = input("Do you want to quit? [y/N] ")
    if quit == "y":
        print("Goodbye!")
    else:
        print("Bye!")

