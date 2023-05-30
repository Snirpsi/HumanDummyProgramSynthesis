#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    return words
</code>
<|/ a |>
<| c |>
Thanks for your help! I used your solution and it worked perfectly!
<|/ c |>
<| c |>
Glad it helped. Don't forget to accept the answer if it solved your problem.
<|/ c |>
<| c |>
I did, thank you! I accepted your answer as soon as I could.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a tags=python |>
<code>
with open('words.txt') as f:
    words = [line.strip() for line in f]
</code>
<|/ a dscore=0 |>
<| c |>
This would only work if the file contains one word per line. OP has multiple words per line.
<|/ c |>
<| c |>
Yes, I know. But the OP didn't mention anything about that. He said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention anything about that. He just said that he was getting an error when he tried to run his code. He didn't mention 