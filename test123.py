from selenium import webdriver
import time
we=webdriver.Firefox()
we.get("http://www.baidu.com")
we.find_element_by_id("kw").send_keys("马云")
we.find_element_by_id("su").click()
time.sleep(8)
we.quit()
