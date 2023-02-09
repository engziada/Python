from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import SessionNotCreatedException, TimeoutException

from time import sleep
# import ChromeDriver
import os 

class AutomationManager():
    path = os.path.dirname(__file__)
    url = "https://visitjordan.gov.jo/travelcars/"

    def Start(self,data):
        try:
            # DRIVER_PATH = path+'\\chromedriver.exe'

            # options = Options()
            options = webdriver.ChromeOptions()
            # options.headless = True
            options.add_argument("start-maximized")
            # options.add_experimental_option("useAutomationExtension", False)
            # options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # options.add_experimental_option('androidPackage', 'com.android.chrome')
            # options.add_argument(f'user-agent={userAgent}')
            # options.add_argument("--window-size=1920,1200")
            # userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36"

            driver = webdriver.Chrome(options=options)

            # try:
            #     driver = webdriver.Chrome(options=options)
            # except SessionNotCreatedException as e:
            #     if ChromeDriver.Latest.Download(path):
            #         try:
            #             driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
            #         except SessionNotCreatedException as e:
            #             print(f"\nRecent version of Chrome Driver has been downloaded to <{path}>, but...", e.msg, sep="\n")
            #             exit(-2)
            #     else:
            #         print("\nCannot download Chrome Driver latest version",e.msg,sep="\n")
            #         exit(-1)

            driver.get(self.url)
            driver.implicitly_wait(30)
            WebDriverWait(driver, 10)

            print('Automation started')

            try:
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID ,"divsubmit")))
                errormsg3 = driver.find_element(By.ID, "divsubmit").text
                print(errormsg3,sep='\n')
                driver.quit()
                print("Site still closed, we will again in 30 seconds")
                sleep(30)
                return(-2,"ظهرت رسالة القدرة الإستيعابية\n" +
                                "سنحاول لاحقا إرسال البيانات مرة أخرى")
            except TimeoutException:
                print("No alert was received")

            #ٌRadio Button
            # <input value="rbEntJor" name="gstdoc" type="radio" id="rbEntJor" class="radiobtns">
            # <input value="rbExtJor" name="gstdoc" type="radio" id="rbExtJor" class="radiobtns">
            # driver.find_element(By.ID, "rbEntJor").click()
            #To click the div
            driver.find_element(By.XPATH, "//div[input[@id='rbEntJor']]").click()

            #TextField: Name
            # <input name="txtName" type="text" maxlength="250" id="txtName" class="form-control custfield" placeholder="ادخل اسمك الكامل">
            driver.find_element(By.ID, 'txtName').send_keys(data['name'])

            # Dropdown list: Nationality
            # <select name = "ddlNationality" id = "ddlNationality" class = "form-control custfield" >
            # <option value = "0" > --- اختر الجنسية - -- < /option >
            # <option value = "99" > الأردن < /option >
            # <option value = "192" > سوريا < /option >
            # </select >
            element=driver.find_element(By.ID, "ddlNationality")
            dropdownlist = Select(element)
            # select.select_by_visible_text('Banana')
            dropdownlist.select_by_value('192')

            #TextField: Passport No
            # <input name = "txtPassportNu" type = "text" maxlength = "10" id = "txtPassportNu" class = "form-control custfield" placeholder = "أدخل رقم جواز السفر" >
            driver.find_element(By.ID, 'txtPassportNu').send_keys(data['passportno'])

            #TextField: IDNumber
            # <input name = "txtIDNumber" type = "text" maxlength = "10" id = "txtIDNumber" class = "form-control custfield" placeholder = "أدخل الرقم الوطني" >
            driver.find_element(By.ID, 'txtIDNumber').send_keys(data['nationalid'])

            #TextField: CarNumber
            # <input name = "txtCarNumber" type = "text" maxlength = "10" id = "txtCarNumber" class = "form-control custfield" placeholder = "أدخل رقم السيارة" >
            driver.find_element(By.ID, 'txtCarNumber').send_keys(data['carnumber'])

            #TextField: Email
            # <input name = "txtEmail" type = "text" maxlength = "150" id = "txtEmail" class = "form-control custfield" onkeypress = "return AvoidSpace()" placeholder = "ادخل بريدك الالكتروني" > 
            driver.find_element(By.ID, 'txtEmail').send_keys(data['email'])

            # Dropdown list: CountryCode
            # <select name = "ddlCountryCode" id = "ddlCountryCode" class = "form-control custfield" >
            # <option value = "0" > رمز الدولة < /option >
            # <option value = "00962" > الأردن - 00962 < /option >
            # <option value = "00963" > سوريا - 00963 < /option >
            # </select >
            element = driver.find_element(By.ID, "ddlCountryCode")
            dropdownlist = Select(element)
            # select.select_by_visible_text('Banana')
            dropdownlist.select_by_value('00963')

            #TextField: Mobile
            # <input name="txtMobile" type="text" maxlength="12" id="txtMobile" class="form-control custfield" placeholder="ادخل رقم اتصال فعال">
            driver.find_element(By.ID, 'txtMobile').send_keys(data['phoneno'])

            #File Upload:
            # <input type = "file" name = "FileUpload2" id = "FileUpload2" style = "display:block !important" >
            driver.find_element(By.ID, 'FileUpload2').send_keys(self.path+"\\"+data['image'])

            #Checkbox
            # <input type = "checkbox" class = "checkboxbtn" id = "chAgreed3" >
            # driver.find_element(By.CSS_SELECTOR, "input[type='checkbox'][id='chAgreed3']").click()
            #To select the DIV element
            driver.find_element(By.XPATH, "//div[input[@id='chAgreed3']]").click()


            #Button: Submit
            # <input type = "submit" name = "SubmitInvest" value = "إرسال الطلب" onclick = "javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;SubmitInvest&quot;, &quot;&quot;, true, &quot;Invest&quot;, &quot;&quot;, false, false))" id = "SubmitInvest" class = "cbtn" >
            driver.find_element(
                By.CSS_SELECTOR, "input[type='submit'][name='SubmitInvest']").click()

            try:
                WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alerttext=alert.text
                alert.accept()
                print("Alert found and accepted\n"+alerttext)
                return(-1,"خطأ فق المدخلات:\n"+alerttext)
            except TimeoutException:
                print("No alert")


            # <div id = "divsubmit" class = "col-lg-12 col-xs-12 errormsg" > نعتذر، القدرة الاستيعابية للتسجيل اكتملت، يرجى المحاولة لاحقاً. < /div >
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID ,"divsubmit")))
                # errormsg1 = driver.find_element(By.ID, "divsubmit").get_attribute('innerText')
                # errormsg2 = driver.find_element(
                #     By.ID, "divsubmit").get_attribute('outerText')
                errormsg3 = driver.find_element(
                    By.ID, "divsubmit").text

                print(errormsg3,sep='\n')
                return(-2,"ظهرت رسالة القدرة الإستيعابية\n" +
                                "سنحاول لاحقا إرسال البيانات مرة أخرى")
            except TimeoutException:
                print("No alert was received, data entered successfully")

                    
            driver.quit()
            return (0,"تم التسجيل بنجاح")
        
        except Exception as e:
            print(e)
            driver.quit()
            return (-3,e)

