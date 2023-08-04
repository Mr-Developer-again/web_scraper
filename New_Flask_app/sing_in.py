from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
def send_email_for_login():
        driver = webdriver.Chrome()
        driver.get("https://medium.com/tag/python/archive/")
        sing_in = driver.find_element(By.CLASS_NAME,"js-signInButton")
        sing_in.click()
        email = driver.find_element(By.CLASS_NAME,"js-emailButton")
        email.click()
        sleep(2)
        input_eamil = driver.find_element(By.ID,"email")
        input_eamil.send_keys("mediumscraper@outlook.com")
        sleep(2)
        click_on_continue = driver.find_element(By.CLASS_NAME , 'button--borderless')
        click_on_continue.click()




################################################################################


# print("sleep for 5 seconde")
# sleep(5)
# input()
# print("sleep for 5 seconde")
# sleep(5)

# elem = driver.find_element(By., "n o ks")


# # print(f"#############this is elem before clear = {elem}############")
# elem.clear()
# # print(f"#############this is elem after clear = {elem}############")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(f"#######this is dirver.page_source = {driver.page_source}##############")
# input()
# assert "No results found." not in driver.page_source
# input()
# driver.close()

# driver = webdriver.Chrome()
# driver.get("https://google.com")
# search = driver.find_element(By.NAME , 'q')
# search.send_keys("selenium")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10)input().until(
#     EC.presence_of_element_located((By.ID, "main"))
# )

# main = driver.find_element(By.ID, "main")
# print(main.text)

