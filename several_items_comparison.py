from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get('https://magento.softwaretestingboard.com/')

#Aqui inicia comparación de varios items (iv)
elem = browser.find_element(By.LINK_TEXT, "Men")
elem.click()

elem = browser.find_element(By.LINK_TEXT, "Tops")
elem.click()

elem = browser.find_element(By.CSS_SELECTOR, ".products-grid .product-image-wrapper")
elem.click()

browser.refresh()

add_to_compare_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "action.tocompare"))
)
add_to_compare_link.click()

elem = browser.find_element(By.LINK_TEXT, "Women")
elem.click()

elem = browser.find_element(By.LINK_TEXT, "Tops")
elem.click()

elem = browser.find_element(By.CSS_SELECTOR, ".products-grid .product-image-wrapper")
elem.click()

browser.refresh()

add_to_compare_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "action.tocompare"))
)
add_to_compare_link.click()

compare_link = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "action.compare"))
)
compare_link.click()

browser.quit()