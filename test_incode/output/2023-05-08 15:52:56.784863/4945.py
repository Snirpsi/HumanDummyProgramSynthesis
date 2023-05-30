#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that enumerates a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html
    #A function that parses the html and extracts the links and titles.
    def extract_links(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        return titles, links
    #A function that parses the html and extracts the links and titles.
    def extract_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        return titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        return titles, links
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links = zip(titles, links)
        return titles_and_links
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles = zip(titles, links, titles)
        return titles_and_links_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles = zip(titles, links, titles, titles)
        return titles_and_links_and_titles_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles_and_titles = zip(titles, links, titles, titles, titles)
        return titles_and_links_and_titles_and_titles_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles_and_titles_and_titles = zip(titles, links, titles, titles, titles, titles)
        return titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles = zip(titles, links, titles, titles, titles, titles, titles)
        return titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles = zip(titles, links, titles, titles, titles, titles, titles, titles)
        return titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles
    #A function that parses the html and extracts the links and titles.
    def extract_links_and_titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles(html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h1')
        links = soup.find_all('a')
        titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles = zip(titles, links, titles, titles, titles, titles, titles, titles, titles, titles, titles)
        return titles_and_links_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_titles_and_title

