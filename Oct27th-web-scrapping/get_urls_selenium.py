from selenium import webdriver
import sys


def initialize_driver():
    try:
        env = sys.platform
        if env == 'win32':
            path = r'C:\Users\user\PycharmProjects\selenium_framework\drivers\chromedriver.exe'
            driver = webdriver.Chrome(path)
            print(f"path : {path} found, chrome driver is initialized")
            return driver
        else:
            path = '/usr/local/bin/chromedriver'
            driver = webdriver.Chrome(path)
            print(f"path : {path} found, chrome driver is initialized")
            return driver
    except Exception as err:
        print(f"{err} : not found, chrome driver is not initialized")


def launch_homepage(driver, url):
    try:
        home_page = driver.get(url)
        driver.maximize_window()
        print(f'{url} : url launched')
    except Exception as err:
        print(f'{url} : url not launched')


def launch_subpages_and_get_html(driver, text, url):
    try:
        for partial_text in text:
            link = driver.find_elements_by_partial_link_text(partial_text)
            link[0].click()
            print(f"Partial link text found, clicked on the link containing {partial_text}")
            html = driver.page_source
            print(html)
            home_page = driver.get(url)
            print(f'{url} : url launched')
    except Exception as err:
        print(f" {err} : Partial link text not found, did not clicked on the link containing {partial_text}")


def main():
    url = 'https://www.python.org/'
    text = ['Key generation', 'Fellow Members', 'already test', 'no longer supported', 'survey']
    driver = initialize_driver()
    launch_homepage(driver, url)
    launch_subpages_and_get_html(driver, text, url)


if __name__ == '__main__':
    main()
