from selenium.webdriver import webdriver
import time
driver = webdriver.Chrome()
driver.get('google.com')
time.sleep(5)
driver.quit()