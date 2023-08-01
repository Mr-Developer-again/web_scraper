import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
####################################################
                    ## get titles ## EveryThing is ok
given_title = os.getenv("TITLE")
driver = webdriver.Chrome()
driver.get(f"https://medium.com/tag/{given_title}/recommended")

main = driver.find_element(By.ID, "root")
articles = main.find_elements(By.TAG_NAME, "article")

for article in articles:
    titles = article.find_element(By.TAG_NAME, "h2")
    link = article.find_elements(By.CSS_SELECTOR, '.af.ag.ah.ai.aj.ak.al.am.an.ao.ap.aq.ar.as.at')[1]
    link_url = link.get_attribute("href")    
    with open("../shared_files/links.text" , 'a') as file :
        file.write(f"{titles.text}==={link_url}\n")
        

