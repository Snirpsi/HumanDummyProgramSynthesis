#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "exit":
            break
        elif answer == "1":
            print("1") 
        elif answer == "2":
            print("2")
        elif answer == "3":
            print("3")
        elif answer == "4":
            print("4")
        elif answer == "5":
            print("5")
        elif answer == "6":
            print("6")
        elif answer == "7":
            print("7")
        elif answer == "8":
            print("8")
        elif answer == "9":
            print("9")
        elif answer == "0":
            print("0")
        else:
            print("Invalid input")
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. I am new to python and have never used the while loop. Can you please explain to me how this works?
<|/ c |>
<| c |>
The `while` loop is used to keep asking the user for input until they enter "exit".  It will keep asking until they enter "exit", then it will break out of the loop.  If you don't understand how it works, you can read up on it here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
<|/ c |>
<| c |>
Thank you for your help. I understand now.
<|/ c |>
<| c |>
No problem.  If you don't understand how it works, you can read up on it here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
<|/ c |>
<| c |>
I understand now. Thank you for your help.
<|/ c |>
<| a tags=python |>
The while loop will keep asking until the user enters exit. 
<code>
while True:
    answer = input("Enter your choice: ")
    if answer == "exit":
        break
    elif answer == "1":
        print("1") 
    elif answer == "2":
        print("2")
    elif answer == "3":
        print("3")
    elif answer == "4":
        print("4")
    elif answer == "5":
        print("5")
    elif answer == "6":
        print("6")
    elif answer == "7":
        print("7")
    elif answer == "8":
        print("8")
    elif answer == "9":
        print("9")
    elif answer == "0":
        print("0")
    else:
        print("Invalid input")
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. I am new to python and have never used the while loop. Can you please explain to me how this works?
<|/ c 