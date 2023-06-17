from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

#Aqui inicia punto 5
element_to_hover = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Women"))
)

actions = ActionChains(browser)
actions.move_to_element(element_to_hover).perform()

element_to_hover = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Tops"))
)

actions = ActionChains(browser)
actions.move_to_element(element_to_hover).perform()

elem = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Hoodies & Sweatshirts"))
)

elem.click()

elem = browser.find_element(By.CSS_SELECTOR, "a.product-item-link[href='https://magento.softwaretestingboard.com/ariel-roll-sleeve-sweatshirt.html']")

elem.click()

browser.refresh()

add_to_compare_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "action.tocompare"))
)
add_to_compare_link.click()


elem = browser.find_element(By.LINK_TEXT, "Men")
elem.click()

elem = browser.find_element(By.LINK_TEXT, "Tops")
elem.click()

elem = browser.find_element(By.CSS_SELECTOR, "a[href='https://magento.softwaretestingboard.com/men/tops-men.html?price=30-40']")
elem.click()

# elem = browser.find_element(By.XPATH, '//a[contains(@class, "swatch-option-link-layered") '
#                                          'and @href="https://magento.softwaretestingboard.com/men/tops-men.html?color=53" '
#                                          'and @aria-label="Green"]')
# elem.click()

#elem = browser.find_element(By.XPATH, 'div[text()="Color"]')
#elem.click()

#elem = browser.find_element(By.CSS_SELECTOR, "a[href='https://magento.softwaretestingboard.com/men/tops-men.html?color=53']")
#elem.click()


#browser.quit()