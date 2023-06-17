from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

# Inicio de sesion
elem = browser.find_element(By.LINK_TEXT, "Sign In")
elem.click()

elem = browser.find_element(By.ID, "email")

# Debe cambiar el email por el que se registró en la creación de la nueva cuenta
elem.send_keys('testuser02@yahoo.com')

elem = browser.find_element(By.ID, "pass")
elem.send_keys('asdf1234%')

elem = browser.find_element(By.ID, "send2")
elem.click()

# Agrega Ariel Roll Sleeve Sweatshirt al carrito
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

time.sleep(1)

# Agrega Deion Long-Sleeve EverCool Tee al carrito
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

# Proceder a realizar la compra
elem = browser.find_element(By.XPATH, "//a[@class='action showcart']")
elem.click()

time.sleep(1)

elem = browser.find_element(By.ID, 'top-cart-btn-checkout')
actions = ActionChains(browser)
actions.move_to_element(elem).perform()
elem.click()

time.sleep(5)

elem = browser.find_element(By.XPATH, "//input[@name='street[0]']")
elem.send_keys("Guadalupe")

elem = browser.find_element(By.XPATH, "//input[@name='city']")
elem.send_keys("San José")

elem = browser.find_element(By.XPATH, "//select[@name='country_id']")
elem.send_keys("Costa Rica")

elem = browser.find_element(By.XPATH, "//input[@name='postcode']")
elem.send_keys("10801")

elem = browser.find_element(By.XPATH, "//input[@name='telephone']")
elem.send_keys("88884444")

time.sleep(5)

next_button = browser.find_element(By.XPATH, "//button[@data-role='opc-continue']")
next_button.click()
time.sleep(5)

place_order_button = browser.find_element(By.XPATH, "//button[@title='Place Order']")
place_order_button.click()
time.sleep(5)

browser.quit()