from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\user\AppData\Roaming\Python\Python37\site-packages\chromedriver_win32"
                          r"\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(5)
driver.find_element_by_name('q').send_keys("Python")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_name('btnK').click()
time.sleep(5)
driver.get("https://www.youtube.com")
time.sleep(5)
driver.find_element_by_name("search_query").send_keys("Python tutorial")
driver.find_element_by_id('search-icon-legacy').click()
time.sleep(5)
driver.minimize_window()
driver.close()