from bs4 import BeautifulSoup
import urllib.request
import re


def get_html(url):
    link_urls1 = []
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    # with open('html.txt','w') as f:
    #     for i in soup:
    #         f.write(str(i))
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        link_urls1.append(link.get('href'))
    sub_str1 = 'feedproxy'
    link_urls2 = []
    for i in link_urls1:
        if sub_str1 in i:
            link_urls2.append(i)
    return link_urls2


def get_html_for_sub_urls(sub_urls):
    for url in sub_urls:
        html = urllib.request.urlopen(url).read()
        print(html)


def main():
    url = 'https://www.python.org/'
    sub_urls = get_html(url)
    get_html_for_sub_urls(sub_urls)


if __name__ == '__main__':
    main()