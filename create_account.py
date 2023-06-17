from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

#Aqui inicia crear cuenta
elem = browser.find_element(By.LINK_TEXT, "Create an Account")
elem.click()

elem = browser.find_element(By.NAME, "firstname")
elem.send_keys('Perico')

elem = browser.find_element(By.NAME, "lastname")
elem.send_keys('Palotes')

elem = browser.find_element(By.NAME, "email")
elem.send_keys('tortuga@yahoo.com')

elem = browser.find_element(By.NAME, "password")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.NAME, "password_confirmation")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.XPATH, "//button[@title='Create an Account']")
elem.click()

browser.quit()