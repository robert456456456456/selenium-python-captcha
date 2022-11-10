import undetected_chromedriver as uc       
import time 
from selenium.webdriver.common.by import By        
from selenium.webdriver.common.keys import Keys        
driver = uc.Chrome()
driver.get("https://accounts.google.com/")
time.sleep(5)        
e = driver.find_element(By.XPATH, '//*[@id="identifierId"]')         
e.send_keys('xxx@gmail.com')        
driver.save_screenshot("02.png")
e.send_keys(Keys.RETURN)
time.sleep(5)        
driver.save_screenshot("03.png")
time.sleep(10)        
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('password')
time.sleep(5)
driver.save_screenshot("04.png")
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(5)
driver.save_screenshot("05.png")
time.sleep(10)
