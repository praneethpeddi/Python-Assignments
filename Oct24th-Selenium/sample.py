from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\user\AppData\Roaming\Python\Python37\site-packages\chromedriver_win32"
                          r"\chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element_by_name('q').send_keys("Python")
driver.maximize_window()
driver.find_element_by_name('btnK').click()
driver.get("https://www.youtube.com")
driver.find_element_by_id("search").send_keys("Python tutorial")
driver.minimize_window()