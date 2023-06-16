from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

elem = browser.find_element(By.LINK_TEXT, "Create an Account")
elem.click()

elem = browser.find_element(By.NAME, "firstname")
elem.send_keys('Perico')

elem = browser.find_element(By.NAME, "lastname")
elem.send_keys('Palotes')

elem = browser.find_element(By.NAME, "email")
elem.send_keys('perico38@yahoo.com')

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
#li_list = browser.find_element(By.XPATH, "//a[@class='action towishlist']")

elem = browser.find_element(By.CSS_SELECTOR, ".products-grid .product-image-wrapper")
elem.click()

browser.refresh()

add_to_wishlist_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "action.towishlist"))
)
add_to_wishlist_link.click()

browser.refresh()

element_to_hover = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//li[@class='product-item']"))
)

actions = ActionChains(browser)
actions.move_to_element(element_to_hover).perform()

remove_item_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn-remove.action.delete"))
)
remove_item_link.click()

#browser.quit()