from bs4 import BeautifulSoup
import urllib.request
import re
import os
import threading
import asyncio


def get_html(url):
    link_urls1 = []
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        link_urls1.append(link.get('href'))
    sub_str1 = 'feedproxy'
    link_urls2 = []
    for i in link_urls1:
        if sub_str1 in i:
            link_urls2.append(i)
    return link_urls2


def create_process(url):
    print(f"ppid : {os.getppid()}, pid : {os.getpid()}")
    html = urllib.request.urlopen(url).read()
    print(html)


def create_thread(url):
    print(f'{threading.current_thread().getName()}, threading started')
    html = urllib.request.urlopen(url).read()
    print(html)


async def create_sub_routine(url):
    # print(f'{asyncio.Task.current_task()}')
    print(f'{asyncio.get_running_loop()}')
    html = urllib.request.urlopen(url).read()
    print(html)


def main():
    url = 'https://www.python.org/'
    sub_urls = get_html(url)
    for url in sub_urls:
        thread = threading.Thread(target=create_thread, args=(url,))
        thread.start()
        thread.join()

    for url in sub_urls:
        pid = os.fork()
        if pid == 0:
            create_process(url)
            break

    for url in sub_urls:
        asyncio.run(create_sub_routine(url))


if __name__ == '__main__':
    main()
