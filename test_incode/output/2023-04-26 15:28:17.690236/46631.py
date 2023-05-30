#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or calculates user input. """    
    
    import sys
    
    word = sys.argv[1]
    
    if len(sys.argv) > 2:
        answer = int(sys.argv[2])
    else:
        answer = int(input("Enter a number: "))
    
    if word == "word":
        print(word)
    elif word == "add":
        print(word + " " + str(answer))
    elif word == "subtract":
        print(word + " " + str(answer))
    elif word == "multiply":
        print(word + " " + str(answer))
    elif word == "divide":
        print(word + " " + str(answer))
    elif word == "quit":
        sys.exit()
    else:
        print("Invalid command")
    
