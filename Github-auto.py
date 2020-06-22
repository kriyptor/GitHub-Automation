#import the webdriver from selenium 
from selenium import webdriver

#Taking User input
ch = int(input("Which Browser Do you want to open: 1>Chrome or 2>Firefox (Enter Number)"))

if(ch==1):

#declare a driver variable
    driver = webdriver.Chrome()

#make a request on the https://github.com/login link
    driver.get('https://github.com/login')

#get the username field using xpath
    Username = driver.find_element_by_xpath('//*[@id="login_field"]')

#send usrename value in the username field
    Username.send_keys('Your UserName')

#get the password field using xpath
    password = driver.find_element_by_xpath('//*[@id="password"]')

#send password value in password field
    password.send_keys('Your Password')

#get the login button using xpath
    loginbtn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

#request for the click on login button
    loginbtn.click()

#get the create button using xpath
    create = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')

#request for the click on create button
    create.click()

#get new repositary button using xpath
    new = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')

#requset for the click on the new repositary button
    new.click()

else:

#declare a driver variable
    driver = webdriver.Firefox(executable_path="C:/Users/sudha/geckodriver.exe")

#make a request on the https://github.com/login link
    driver.get('https://github.com/login')

#get the username field using xpath
    Username = driver.find_element_by_xpath('//*[@id="login_field"]')

#send usrename value in the username field
    Username.send_keys('UserName')

#get the password field using xpath 
    password = driver.find_element_by_xpath('//*[@id="password"]')

#send password value in password field
    password.send_keys('Password')

#get the login button using xpath
    loginbtn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

#request for the click on login button
    loginbtn.click()

#get the create button using xpath
    create = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/summary')

#request for the click on create button
    create.click()

#get new repositary button using xpath
    new = driver.find_element_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')

#requset for the click on the new repositary button
    new.click()

# ------End------
