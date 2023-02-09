#from itertools import product
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# from urllib.request import Request, urlopen
# import mechanicalsoup
#import urllib
# from bs4 import BeautifulSoup

# browser = mechanicalsoup.Browser()
url = "https://brantu.com/eg-en/latest-arrivals"

# req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
# html = urlopen(req).read().decode("utf-8")
# soup = BeautifulSoup(html, 'html.parser')

#page = urlopen(url)
#print(page)

# html = page.read().decode("utf-8")

# page = browser.get(url)
# html=page.soup
# product_card = html.select("div", class_="contain-product")  # {"class": "contain-product"})
# print(product_card)

# {"class": "contain-product"})
# product_card = soup.find_all("div", class_="contain-product")
# product_card = soup.select('div.contain-product')
# print(product_card)


DRIVER_PATH = 'c:/chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")



# my_element_id = 'something123'
# ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
# your_element = WebDriverWait(driver, some_timeout, ignored_exceptions=ignored_exceptions)\
#     .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(url)
sleep(5)

count=0
length = 1
while length > 0 and count <5:
    try:
        images = list(map(lambda img: img .get_attribute('src'), driver.find_elements(By.TAG_NAME, "img")))
        placeholders = list(filter(lambda img: "placeholders" in img, images))
        length=len(placeholders)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Count: {count}, Length: {length}")
        sleep(5)
        count+=1
    except (NoSuchElementException, StaleElementReferenceException):
        count+1
        continue



count=1
web_elements = driver.find_elements(By.CLASS_NAME, 'contain-product')
# h1 = driver.find_elements(By.CSS_SELECTOR, 'div.contain-product')
for element in web_elements:
    # if not element.is_displayed(): continue
    print(f"Number ({count}):")
    print(element.text)
    img=element.find_element(By.TAG_NAME,"img")
    print(img.get_attribute('src'))
    count+=1

driver.quit()

