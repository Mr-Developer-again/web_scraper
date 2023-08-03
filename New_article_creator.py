import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Reading links from file
with open('New_links.text' , 'r') as file:
    all_text = file.readlines()
    for text in all_text:
        val = text.split("===")    
            
        url = val[1]
        file_name = val[0]
        driver.get(url)

        # Find the element and get its text content
        element = driver.find_element(By.TAG_NAME , "article")
        text = element.text
        with open(f'./articles/{file_name}.txt' , 'a') as f :
            f.write(text)



