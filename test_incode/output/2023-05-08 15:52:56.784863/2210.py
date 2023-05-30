#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that stores a http request.
    while True:
        try:
            req = requests.get(url)
            req.raise_for_status()
            soup = BeautifulSoup(req.text, 'html.parser')
            title = soup.find('h1', {'class': 'title'}).text
            content = soup.find('div', {'class': 'content'}).text
            date = soup.find('div', {'class': 'date'}).text
            author = soup.find('div', {'class': 'author'}).text
            url = soup.find('div', {'class': 'url'}).text
            
            
            print(title, content, date, author, url)
            
        except:
            print("No more pages")
            break

