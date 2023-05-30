#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or enumerates fruits. """    
    while True:
        try:
            fruits = input("Enter a fruit: ")
            fruits = fruits.split()
            fruits = [int(x) for x in fruits]
            print(fruits)
        except ValueError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("Program terminated")
            break
</code>
<|/ a dscore=1 |>
<| a dscore=0 |>
<code>
fruits = input("Enter a fruit: ")
fruits = fruits.split()
fruits = [int(x) for x in fruits]
print(fruits)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Please don't post only code as an answer, but also provide an explanation what your code does and how it solves the problem of the question. Answers with an explanation are usually more helpful and of better quality, and are more likely to attract upvotes.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
while True:
    try:
        fruits = input("Enter a fruit: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        print(fruits)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Program terminated")
        break
</code>
<|/ a dscore=0 |>
<| a tags=python,python-3.x |>
<code>
while True:
    try:
        fruits = input("Enter a fruit: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        print(fruits)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Program terminated")
        break
</code>
<|/ a dscore=0 |>
<| a tags=python,python-3.x |>
<code>
while True:
    try:
        fruits = input("Enter a fruit: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        print(fruits)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Program terminated")
        break
</code>
<|/ a dscore=0 |>
<| a |>
<code>
while True:
    try:
        fruits = input("Enter a fruit: ")
        fruits = fruits.split()
        fruits = [int(x) for x in fruits]
        print(fruits)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Program terminated")
        break
</code>
<|/ a dscore=0 tags=python,python-3.x |>