#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == numbers[-2]:
            break
    print('The numbers are: ', end='')
    for number in numbers:
        print(number, end='')
    print('')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I'm still new to programming and I still don't understand what your code is doing. Could you explain it to me a little bit more? Thanks!
<|/ c |>
<| c |>
I added a brief explanation to the answer.
<|/ c |>
<| c |>
Thanks so much! This helped me a lot! I understand it now!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
