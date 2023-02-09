import contextlib
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from time import sleep

url = "https://visitjordan.gov.jo/travelcars/"
DRIVER_PATH = 'c:/chromedriver.exe'
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"


options = Options()
# options.headless = True
options.add_argument("start-maximized")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')

# options.add_argument("--window-size=1920,1200")
# userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36"

# my_element_id = 'something123'
# ignored_exceptions = (NoSuchElementException,StaleElementReferenceException,)
# your_element = WebDriverWait(driver, some_timeout, ignored_exceptions=ignored_exceptions)\
#     .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))


driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.implicitly_wait(10)
driver.get(url)

#Google Login
# ChromeOptions options = new ChromeOptions()
# options.addArguments("start-maximized")
# options.setExperimentalOption("useAutomationExtension", false)
# options.setExperimentalOption(
#     "excludeSwitches", Collections.singletonList("enable-automation"))
# WebDriver driver = new ChromeDriver(options)
# driver.get("https://accounts.google.com/signin")
# new WebDriverWait(driver, 10).until(ExpectedConditions.elementToBeClickable(By.xpath("//input[@id='identifierId']"))).sendKeys("gashu")
# driver.findElement(By.id("identifierNext")).click()
# new WebDriverWait(driver, 10).until(ExpectedConditions.elementToBeClickable(By.xpath("//input[@name='password']"))).sendKeys("gashu")
# driver.findElement(By.id("passwordNext")).click()
# System.out.println(driver.getTitle())

#Login
if driver.title.find("Sign in")!=-1:
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
        By.ID, "_email"))).send_keys("MuhammadAhmadZiada@gmail.com")
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
        By.ID, "_password"))).send_keys("mazisvip")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((
        By.ID, "submit"))).click()


#Skip the modal
with contextlib.suppress(NoSuchElementException):
    modal = driver.find_element(By.CLASS_NAME, 'modal-content')
    modal.find_element(By.CLASS_NAME, "close").click()

#Get data
candItems = driver.find_elements(By.CLASS_NAME, 'sp-candItem')
for count, candItem in enumerate(candItems, start=1):
    print(f"Number ({count}):")
    # print(candItem.text)
    candItem_main = candItem.find_element(By.CLASS_NAME, "sp-candItem__main")
    candItem_main.click()

    #Open Details
    cand_details=WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
        By.CLASS_NAME, "c-cand-detail")))
    #Reveal contacts
    # driver.find_element_by_css_selector(
    #     "table.BaseTable tr.SelPrimary td > span:first-child").click()
    cand_details.find_element(By.CLASS_NAME, "btn-wrap").click()
    cand_profile = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((
        By.CLASS_NAME, "profile-item")))
    map(lambda span:span.click(), cand_details.find_elements(By.TAG_NAME, "span"))
    print(cand_details.text)
    

    # print(f"Name: {candItem_name}", f"Title: {candItem_title}",
    #       f"Employer: {candItem_company}", f"Address: {candItem_city}", f"Url: {candItem_link}",sep="\n")

driver.quit()

