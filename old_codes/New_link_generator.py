import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
####################################################
                    ## get titles ## EveryThing is ok
# given_title = os.getenv("TITLE")
years = ['2018' , '2019' , '2020' , '2021' , '2022' , '2023']
driver = webdriver.Chrome()
for index in years:
    driver.get(f"https://medium.com/tag/python/archive/{index}")
    main = driver.find_element(By.TAG_NAME, "body")

    articles = main.find_elements(By.CLASS_NAME, "streamItem--postPreview")

    for article in articles:
        titles = article.find_element(By.TAG_NAME, "h3")
        print(titles.text)
        link = article.find_elements(By.TAG_NAME, 'a')[3]
        link_url = link.get_attribute("href")  
        with open("New_links.text" , 'a') as file :
            file.write(f"{titles.text}==={link_url}\n")
        