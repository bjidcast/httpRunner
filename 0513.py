from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
driver = webdriver.Chrome()




driver.get("https://www.baidu.com")
#定位元素，利于封装

driver.find_element(By.ID,"kw").send_keys("测试一下")
