#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or enumerates words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number')
        else:
            if number > len(words):
                print('Too many words')
            else:
                words.append(number)
                print('Added {}'.format(number))
                break
    print('Done')
</code>
<|/ a dscore=0 |>
<| c |>
This does not answer the question
<|/ c |>
<| c |>
It does answer the question. He wants to know how to make a loop that adds numbers to a list until he gets a number greater than the size of the list. He doesn't know how to do that. He wants to know how to make a loop that adds a number to a list until he gets a number greater than the size of the list.
<|/ c |>
<| c |>
I agree with your comment and I agree with your answer. My answer does exactly what the OP asked for. Your answer does not answer the question at all. Your answer does not answer the question at all.
<|/ c |>
<| c |>
The OP asked how to make a loop that adds numbers to a list until he gets a number greater than the size of the list. Your answer does not answer the question at all.
<|/ c |>
<| c |>
The OP asked how to make a loop that adds numbers to a list until he gets a number greater than the size of the list. Your answer does not answer the question at all.
<|/ c |>
<| a dscore=0 |>
You can use a while loop to do that:
<code>
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
while True:
    number = int(input('Enter a number: '))
    if number > len(words):
        print('Too many words')
    else:
        words.append(number)
        print('Added {}'.format(number))
        break
</code>
<|/ a tags=python |>
<| c |>
This does not answer the question
<|/ c |>
<| c |>
This does not answer the question. He wants to know how to make a loop that adds numbers to a list until he gets a number greater than the size of the list. He doesn't know how to do that. He wants to know how to make a loop that adds a number to a list until he gets a number greater than the size of the list.
<|/ c |>
<| c |>
I agree with your comment and I agree with your answer. My answer does exactly 