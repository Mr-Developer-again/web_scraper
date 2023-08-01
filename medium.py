from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
####################################################
                    ## get titles ## EveryThing is ok
# val = 1
# driver = webdriver.Chrome()
# driver.get("https://medium.com/tag/cpp/recommended")

# main = driver.find_element(By.ID, "root")
# articles = main.find_elements(By.TAG_NAME, "article")

# for article in articles:
#     titles = article.find_element(By.TAG_NAME, "h2")
#     # writer = article.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[4]/div/div[1]/div[1]/article/div/div/div/div/div[1]/div[2]/div/div/a/p')
#     link = article.find_elements(By.CSS_SELECTOR, '.af.ag.ah.ai.aj.ak.al.am.an.ao.ap.aq.ar.as.at')[1]
#     link_url = link.get_attribute("href")
#     print(f"########## the title nubmer is {val} ##########\n{titles.text}\nthe link is : \n{link_url}\n\n")
#     val += 1

# input()





##################################################
        #### Login #### 
        # SomeThing don't work , and there is some bug in the class_name . i did solve this problem in the above code (by use css and deleting the spaces)
# print("before Chrome")
# driver = webdriver.Chrome()
# print("after Chrome")
# driver.get("https://medium.com")
# root = driver.find_element(By.ID ,'root')
# sing_in = root.find_elements(By.CSS_SELECTOR, '.bd.be.bf.bg.bh.bi.bj.bk.bl.bm.bn.bo.bp.bq.br')[4]
# sing_in.click()
# # email = sing_in.find_element(By.TAG_NAME, 'button')
# # root2 = root.find_element(By.LINK_TEXT, 'Sign in with email')
# root2 = root.find_element(By.CSS_SELECTOR, '.by.b.eg.ef.cb.ny.nc.nz.oa.ob.cj.ck.cp.de.oc.od.oe.of.cq.cr.cs.ct.cu')
# root2.click()


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

# # try:
# #     main = WebDriverWait(driver, 10)
# # input().until(
# #     EC.presence_of_element_located((By.ID, "main"))
# # )

# main = driver.find_element(By.ID, "main")
# print(main.text)


##########################################################################
            #### geting all of content of one article

driver = webdriver.Chrome()

# Load the website
url = "https://medium.com/@maityamit/dsa-with-c-handwritten-notes-amit-maity-130-pages-2c2231e8bf57?source=tag_recommended_feed---------9-85----------cpp----------b3f445b5_527d_4222_9843_47903a0f8995-------"
driver.get(url)

# Find the element and get its text content
element = driver.find_element(By.TAG_NAME , "article")
text = element.text

# Print the text content
print(text)


############################################################################
            ##### 
            
