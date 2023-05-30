#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that enumerates user input.
    while True:
        choice = input("Enter your choice: ")
        if choice == "exit":
            break
        elif choice == "1":
            one()
        elif choice == "2":
            two()
        elif choice == "3":
            three()
        elif choice == "4":
            four()
        elif choice == "5":
            five()
        elif choice == "6":
            six()
        elif choice == "7":
            seven()
        elif choice == "8":
            eight()
        elif choice == "9":
            nine()
        else:
            print("Invalid choice.")

