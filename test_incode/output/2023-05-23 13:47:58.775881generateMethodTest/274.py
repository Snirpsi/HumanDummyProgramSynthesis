#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that adds a port.
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I tried your solution and it works perfectly for me. However I still have one question: how do I access the port number from my browser? I tried to access it by typing `localhost:8080` but it doesn't work. Do I have to configure something in Apache? I tried to access it by typing `localhost:8080/` but it doesn't work either. Do I have to configure something in Apache?
<|/ c |>
<| c |>
I added a link to my answer that explains how to access the port number from your browser. Hope it helps.
<|/ c |>
<| c |>
Thanks a lot! I really appreciate your help.
<|/ c |>
<| a dscore=0 |>
I used the answer from to solve my problem. 
I added the following lines to my httpd.conf file:
<code>
<VirtualHost *:80>
    ServerName localhost
    ServerAlias localhost
    DocumentRoot /var/www/html
    <Directory /var/www/html>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Order allow,deny
        allow from all
    </Directory>
</VirtualHost>
</code>
I then added the following lines to my .htaccess file:
<code>
RewriteEngine on
RewriteCond %{SERVER_PORT} !^443$
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</code>
I then restarted the Apache server and now I can access my website by typing localhost:8080 instead of localhost:8080/
<|/ a tags=apache,python,flask,flask-restful |>
<| c |>
This does not answer the question. Your answer does not solve the problem of accessing the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to access the port number from your browser. Your answer does not explain how to 