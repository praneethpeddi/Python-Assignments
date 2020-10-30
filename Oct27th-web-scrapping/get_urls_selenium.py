from selenium import webdriver

try:
    path = r'C:\Users\user\PycharmProjects\selenium_framework\drivers\chromedriver.exe'
    driver = webdriver.Chrome(path)
    print(f"{path} : found, chrome driver is initialized")
except Exception as err:
    print(f"{err} : not found, chrome driver is not initialized")


def launch_homepage(url):
    try:
        home_page = driver.get(url)
        print(f'{url}, launched')
    except Exception as err:
        print(err)


def launch_subpages(text):
    try:
        for i in text:
            link = driver.find_elements_by_partial_link_text(i)
            link.click()
    except Exception as err:
        print(err)


def main():
    url = 'https://www.python.org/'
    text = ['Key generation', 'Fellow Members', 'already test', 'no longer supported', 'share and learn']
    launch_homepage(url)
    launch_subpages(text)


if __name__ == '__main__':
    main()
