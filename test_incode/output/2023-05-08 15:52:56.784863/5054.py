#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that returns a http request.
    def request():
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()
    #The function that returns the response of the http request.
    def response():
        return request()
    #The function that returns the response of the http request.
    content = response()
    #The function that returns the response of the http request.
    soup = BeautifulSoup(content, 'html.parser')
    #The function that returns the response of the http request.
    title = soup.find('h1')
    #The function that returns the response of the http request.
    link = soup.find('a')
    #The function that returns the response of the http request.
    content = soup.find('div', class_='content')
    #The function that returns the response of the http request.
    content = content.text
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.
    content = content.strip()
    #The function that returns the response of the http request.
    content = content.split('\n')
    #The function that returns the response of the http request.
    content = content[0]
    #The function that returns the response of the http request.


