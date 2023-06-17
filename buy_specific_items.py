from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

#Login
# elem = browser.find_element(By.LINK_TEXT, "Sign In")
# elem.click()

# elem = browser.find_element(By.ID, "email")
# elem.send_keys('snoopie7@yahoo.com')

# elem = browser.find_element(By.ID, "pass")
# elem.send_keys('asdf1234%')

# elem = browser.find_element(By.ID, "send2")
# elem.click()

#Aqui inicia crear cuenta
elem = browser.find_element(By.LINK_TEXT, "Create an Account")
elem.click()

elem = browser.find_element(By.NAME, "firstname")
elem.send_keys('Perico')

elem = browser.find_element(By.NAME, "lastname")
elem.send_keys('Palotes')

elem = browser.find_element(By.NAME, "email")
elem.send_keys('geko3@yahoo.com')

elem = browser.find_element(By.NAME, "password")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.NAME, "password_confirmation")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.XPATH, "//button[@title='Create an Account']")
elem.click()



#Aqui inicia punto 5
#Agrega Ariel Roll Sleeve Sweatshirt al carrito
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

elem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "option-label-size-143-item-166"))
)
elem.click()

elem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "option-label-color-93-item-53"))
)
elem.click()

add_to_cart = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "product-addtocart-button"))
)
add_to_cart.click()

time.sleep(5)
#Agrega Deion Long-Sleeve EverCool™ Tee al carrito
elem = browser.find_element(By.LINK_TEXT, "Men")
elem.click()

elem = browser.find_element(By.LINK_TEXT, "Tops")
elem.click()

elem = browser.find_element(By.XPATH, '//div[text()="Price"]')
actions = ActionChains(browser)
browser.execute_script("arguments[0].scrollIntoView();", elem)
actions.move_to_element(elem).perform()
elem.click()

elem = browser.find_element(By.XPATH, '//span[text()="$30.00"]')
elem.click()

elem = browser.find_element(By.XPATH, '//div[text()="Color"]')
actions = ActionChains(browser)
browser.execute_script("arguments[0].scrollIntoView();", elem)
actions.move_to_element(elem).perform()
elem.click()
elem = browser.find_element(By.XPATH, '//div[@class="swatch-option color " and @tabindex="-1" and @option-type="1" and @option-id="53" and @option-label="Green"]')
elem.click()

elem = browser.find_element(By.CSS_SELECTOR, ".products-grid .product-image-wrapper")
elem.click()

browser.refresh()

elem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "option-label-size-143-item-166"))
)
elem.click()

elem = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "option-label-color-93-item-53"))
)
elem.click()

add_to_cart = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "product-addtocart-button"))
)
add_to_cart.click()


#Proceder a realizar la compra
elem = browser.find_element(By.XPATH, "//a[@class='action showcart']")
elem.click()

# elem = browser.find_element(By.ID, "top-cart-btn-checkout")
# elem.click()

elem = browser.find_element(By.ID, 'top-cart-btn-checkout')
actions = ActionChains(browser)
actions.move_to_element(elem).perform()
elem.click()


#elem = browser.find_element(By.XPATH, "//input[@name='street[0]']")
#elem.send_keys("aaaaaaaaaa")

#city = browser.find_element(By.XPATH, "//input[@name='city']")
#city.send_keys("Rohrmoser")
#time.sleep(1)

#country = browser.find_element(By.XPATH, "//select[@name='country_id']")
#country.send_keys("Costa Rica")
#time.sleep(1)

#zip = browser.find_element(By.XPATH, "//input[@name='postcode']")
#zip.send_keys("10109")
#time.sleep(1)

#phone = browser.find_element(By.XPATH, "//input[@name='telephone']")
#phone.send_keys("84272458")
#time.sleep(3)

# press next button
# next_button = browser.find_element(
#     By.XPATH, "//button[@data-role='opc-continue']"
# )
# next_button.click()
# time.sleep(5)

# # press place order button
# place_order_button = browser.find_element(
#     By.XPATH, "//button[@title='Place Order']"
# )
# place_order_button.click()
# time.sleep(5)
#browser.quit()