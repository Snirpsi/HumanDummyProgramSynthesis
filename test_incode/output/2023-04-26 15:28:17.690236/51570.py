#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or multiplyes user input. """    
    while True:
        answer = input('Do you want to continue? [y/n] ')
        if answer.lower() == 'y':
            break
        elif answer.lower() == 'n':
            break
        else:
            print('Invalid input.')
            continue
    print('Goodbye!')
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. Unfortunately this doesn't solve my problem because I still need to have the user input in the while loop. Do you know how I can achieve that?
<|/ c |>
<| c |>
I added an example to my answer. Hope this helps.
<|/ c |>
<| c |>
Thank you for your answer. Unfortunately this doesn't solve my problem because I still need to have the user input in the while loop. Do you know how I can achieve that?
<|/ c |>
<| c |>
I added an example to my answer. Hope this helps.
<|/ c |>
<| c |>
Thank you for your answer. Unfortunately this doesn't solve my problem because I still need to have the user input in the while loop. Do you know how I can achieve that?
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    answer = input('Do you want to continue? [y/n] ')
    if answer.lower() == 'y':
        break
    elif answer.lower() == 'n':
        break
    else:
        print('Invalid input.')
        continue
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you for your answer. Unfortunately this doesn't solve my problem because I still need to have the user input in the while loop. Do you know how I can achieve that?
<|/ c |>
<| c |>
I added an example to my answer. Hope this helps.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
while True:
    answer = input('Do you want to continue? [y/n] ')
    if answer.lower() == 'y':
        break
    elif answer.lower() == 'n':
        break
    else:
        print('Invalid input.')
        continue
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. Unfortunately this doesn't solve my problem because I still need to have the user input in the while loop. Do you know how I can achieve that?
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    answer = input('Do you want to continue? [y/n] ')
    if answer.lower() == 'y':
        break
    elif answer.lower() == 'n':
        break
    else:
        print('Invalid input.')
        continue
