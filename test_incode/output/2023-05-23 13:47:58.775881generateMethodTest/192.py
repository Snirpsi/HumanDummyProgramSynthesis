#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that calculates a http request.
    def http_request(url):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            html = response.read()
            return html
        except urllib.error.URLError as e:
            print(e)
            return ""
    #A function that parses the html and returns the data as a string.
    def parse_html(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a list.
    def parse_html_list(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a dictionary.
    def parse_html_dict():
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a list.
    def parse_html_list(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a dictionary.
    def parse_html_dict():
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a list.
    def parse_html_list(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a dictionary.
    def parse_html_dict():
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a list.
    def parse_html_list(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a dictionary.
    def parse_html_dict():
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a list.
    def parse_html_list(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
        body = []
        for row in rows:
            body.append(row.find_all('td')[1].text)
        return header, body
    #A function that parses the html and returns the data as a dictionary.
    def parse_html_dict():
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-condensed'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('td')[0].text)
