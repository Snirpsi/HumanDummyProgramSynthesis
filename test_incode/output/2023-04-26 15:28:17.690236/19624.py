#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or calculates words. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "":
            break
        elif answer == "1":
            answer = 1
        elif answer == "2":
            answer = 2
        elif answer == "3":
            answer = 3
        elif answer == "4":
            answer = 4
        elif answer == "5":
            answer = 5
        elif answer == "6":
            answer = 6
        elif answer == "7":
            answer = 7
        elif answer == "8":
            answer = 8
        elif answer == "9":
            answer = 9
        elif answer == "0":
            answer = 0
        else:
            print("Sorry, I didn't understand that.")
    
    print("The word was", answer)
    
