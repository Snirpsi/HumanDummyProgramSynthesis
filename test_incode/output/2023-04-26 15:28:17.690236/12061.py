#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and converts a list of words. """    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        words = input("Enter a word: ")
        words = words.split()
        for word in words:
            if word in numbers:
                numbers.remove(word)
            else:
                print("That word is not in the list")
                break
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer, but i need it to print out a list that has all the numbers and words that have been entered and that are not in the list
<|/ c |>
<| c |>
