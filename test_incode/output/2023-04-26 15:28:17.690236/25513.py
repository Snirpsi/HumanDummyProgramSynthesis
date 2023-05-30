#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    httpd = HTTPServer(('', 8080), FruitHandler)
    print('serving at http://localhost:8080')
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I'm a beginner in Python and web development, so I didn't understand your solution. Could you please explain it to me a little bit more?
<|/ c |>
<| c |>
I added a brief explanation to the answer.
<|/ c |>
<| c |>
Thanks a lot! It works perfectly!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
