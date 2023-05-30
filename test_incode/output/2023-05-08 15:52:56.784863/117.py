#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that opens a list of words.
    #It then prints them out in reverse order.
    #It then asks the user if they want to continue or not.
    wordlist = input("Enter a list of words: ")
    wordlist = wordlist.split()
    wordlist.sort(reverse = True)
    print(wordlist)
    continue_ask = input("Do you want to continue (y/n)? ")
    if continue_ask == "y":
        print("Thank you for using my program!")
    else:
        print("Goodbye!")

