#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that requests a http request.
    while True:
        try:
            req = requests.get(url)
            if req.status_code == 200:
                response = req.text
                soup = BeautifulSoup(response, 'html.parser')
                title = soup.find('h1', {'class': 'title'}).text
                link = soup.find('a', {'class': 'link'}).get('href')
                date = soup.find('span', {'class': 'date'}).text
                author = soup.find('span', {'class': 'author'}).text
                content = soup.find('div', {'class': 'content'}).text
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()
                content = content.strip()
                author = author.strip()
                title = title.strip()
                link = link.strip()
                date = date.strip()


