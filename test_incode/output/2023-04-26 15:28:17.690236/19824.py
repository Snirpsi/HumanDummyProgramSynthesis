#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == "exit":
            break
        elif choice == "1":
            print("1")
        elif choice == "2":
            print("2")
        elif choice == "3":
            print("3")
        elif choice == "4":
            print("4")
        elif choice == "5":
            print("5")
        elif choice == "6":
            print("6")
        elif choice == "7":
            print("7")
        elif choice == "8":
            print("8")
        elif choice == "9":
            print("9")
        elif choice == "0":
            print("0")
        else:
            print("Invalid choice.")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, it works. But I still don't understand why the code doesn't work if I put it in a separate file instead of in the main file.
<|/ c |>
<| c |>
I believe that your code is working fine. Maybe the problem is that you didn't import the file in the main file?
<|/ c |>
<| c |>
Yes, I imported the file in the main file. But I still don't understand why the code doesn't work if I put it in a separate file instead of in the main file.
<|/ c |>
<| c |>
I updated my answer. Maybe that helps.
<|/ c |>
<| c |>
Thanks, it works. But I still don't understand why the code doesn't work if I put it in a separate file instead of in the main file.
<|/ c |>
<| a dscore=0 |>
<code>
def convert():
    while True:
        choice = input("Enter your choice: ")
        if choice == "exit":
            break
        elif choice == "1":
            print("1")
        elif choice == "2":
            print("2")
        elif choice == "3":
            print("3")
        elif choice == "4":
            print("4")
        elif choice == "5":
            print("5")
        elif choice == "6":
            print("6")
        elif choice == "7":
            print("7")
        elif choice == "8":
            print("8")
        elif choice == "9":
            print("9")
        elif choice == "0":
            print("0")
        else:
            print("Invalid choice.")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, it works. But I still don't understand why the code doesn't work if I put it in a separate file instead of in the main file.
<|/ c |>
<| a |>
<code>
def convert():
    while True:
        choice = input("Enter your choice: ")
        if choice == "exit":
