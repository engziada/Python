import requests
import mechanicalsoup
import os

url = "https://visitjordan.gov.jo/travelcars/"
name = 'محمد محمود عقيل'
direction = 'دخول'
nationality = 'سوري'
passportno = 'NO12388953'
nationalid = '1003837044'
carnumber = '228232'
email = 'abdalghne.karoof@gmail.com'
cc = ''
phoneno = '0968859388'
image = 'IMG-20230130-WA0026.jpg'
status = -2
log = ''

# browser = mechanicalsoup.StatefulBrowser()
# browser.open(url)
# form=browser.select_form('form[id="form1"]')
# # browser.form.print_summary()
# browser["gstdoc"] = "rbEntJor"
# browser["txtName"] = name
# browser["txtPassportNu"] = passportno
# browser["txtIDNumber"] = nationalid
# browser["txtCarNumber"] = carnumber
# browser["txtEmail"] = email
# browser["ddlCountryCode"] = "00963"
# browser["txtMobile"] = phoneno
# # browser["hdFileUpload2"] = os.path.dirname(__file__)+"\\"+image
# form.set('hdFileUpload2', os.path.dirname(__file__)+"\\"+image)
# # browser["chAgreed3"] = "checked"
# browser.page.find(type='checkbox').checked = 'checked'
# response = browser.submit_selected()
# print(response)
# browser.launch_browser()




payload = {
    "gstdoc":"rbEntJor",
    "txtName":name,
    "txtPassportNu":passportno,
    "txtIDNumber":nationalid,
    "txtCarNumber":carnumber,
    "txtEmail": email,
    "ddlCountryCode":"00963",
    "txtMobile":phoneno,
    # form.set('hdFileUpload2', os.path.dirname(__file__)+"\\"+image)
    # # browser["chAgreed3"] = "checked"
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Form submission succeeded")
else:
    print("Form submission failed")
