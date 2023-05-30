#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or opens fruits. """    
    while True:
        try:
            fruit = int(input("Enter a number or open a fruit: "))
            if fruit == 1:
                print("Apple")
            elif fruit == 2:
                print("Banana")
            elif fruit == 3:
                print("Orange")
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
        except EOFError:
            print("Bye")
        except KeyboardInterrupt:
            print("Bye")
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the answer. Can you explain to me what does "except EOFError:" do?
<|/ c |>
<| c |>
It catches EOFError and exits the loop. EOFError is thrown when the user presses the EOF key on the keyboard. EOFError is also thrown when an invalid input is entered.
<|/ c |>
<| c |>
Thanks so much! I understand now.
<|/ c |>
<| c |>
You're welcome. Glad I could help.
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    try:
        fruit = int(input("Enter a number or open a fruit: "))
        if fruit == 1:
            print("Apple")
        elif fruit == 2:
            print("Banana")
        elif fruit == 3:
            print("Orange")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
    except EOFError:
        print("Bye")
    except KeyboardInterrupt:
        print("Bye")
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Please add some explanation to your answer
<|/ c |>
<| c |>
Thanks for the answer. Can you explain to me what does "except EOFError:" do?
<|/ c |>
<| c |>
It catches EOFError and exits the loop. EOFError is thrown when the user presses the EOF key on the keyboard. EOFError is also thrown when an invalid input is entered.
<|/ c |>
<| c |>
Thanks so much! I understand now.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
while True:
    try:
        fruit = int(input("Enter a number or open a fruit: "))
        if fruit == 1:
            print("Apple")
        elif fruit == 2:
            print("Banana")
        elif fruit == 3:
            print("Orange")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
    except EOFError:
        print("Bye")