from selenium import webdriver
import sys
import time


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


def verify_login(driver):
    try:
        username_field = driver.find_elements_by_id('identifierId')
        print(f"Username field exits")
        if username_field:
            driver.find_elements_by_name('identifier')[0].send_keys('praneethpeddi1995')
            print(f"Entered the email id")
            driver.find_elements_by_class_name('VfPpkd-RLmnJb')[0].click()
            time.sleep(10)
            print(f"Clicked on next button")
        else:
            print('username field does not exits')
    except Exception as error:
        print(f"Exception : {error}")


def main():
    url = 'https://www.gmail.com/'
    driver = initialize_driver()
    launch_homepage(driver, url)
    verify_login(driver)


if __name__ == '__main__':
    main()