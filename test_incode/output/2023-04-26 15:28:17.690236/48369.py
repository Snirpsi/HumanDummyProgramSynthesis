#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter a number: ")
        try:
            answer = int(answer)
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        else:
            break
    print("The number was", answer)
</code>
<|/ a |>
<| c |>
Thanks for the 