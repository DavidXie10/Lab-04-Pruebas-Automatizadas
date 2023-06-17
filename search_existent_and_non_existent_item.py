from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

#Aqui busca item existente
search_input_existent_item = browser.find_element(By.NAME, "q")

search_input_existent_item.send_keys("Cassius Sparring Tank" + Keys.ENTER)

time.sleep(2)

#Aqui busca items no existentes

search_input_non_existent = browser.find_element(By.NAME, "q")

search_input_non_existent.clear()

search_input_non_existent.send_keys("Pollo")

search_input_non_existent.send_keys(Keys.ENTER)

time.sleep(2)

browser.quit()