from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

elem = browser.find_element(By.LINK_TEXT, "Create an Account")
elem.click()

elem = browser.find_element(By.NAME, "firstname")
elem.send_keys('Perico')

elem = browser.find_element(By.NAME, "lastname")
elem.send_keys('Palotes')

elem = browser.find_element(By.NAME, "email")
elem.send_keys('perico15@yahoo.com')

elem = browser.find_element(By.NAME, "password")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.NAME, "password_confirmation")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.XPATH, "//button[@title='Create an Account']")
elem.click()

#Aqui hacer la prueba
# elem = browser.find_element(By.XPATH, "//html/body/div[1]/div/div/div[2]/nav/ul/li[3]/a/span[2]")
# elem.click()

elem = browser.find_element(By.LINK_TEXT, "Men")
elem.click()

elem = browser.find_element(By.LINK_TEXT, "Tops")
elem.click()

# Find the list of <li> elements
li_list = browser.find_element(By.XPATH, "//a[@class='action towishlist']")

first_li = li_list[0]
first_li.click()

# elem = browser.find_element(By.CLASS_NAME, "item product product-item")
# elem.click()

#elem = browser.find_element(By.LINK_TEXT, "Remove Item")
#elem.click()



# elem = browser.find_element(By.XPATH, "//html/body/div[1]/main/div[4]/div[2]/div[1]/div[2]/dl/dd/ol/li[1]/a")
# elem.click()

#elem = browser.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[2]/a[1]")
#elem.click()

#browser.quit()