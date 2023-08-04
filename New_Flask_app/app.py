from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask , render_template , request , url_for , redirect
from sing_in import send_email_for_login
from read_email import read_email_for_login , regex_and_find_link

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/title')
def get_title():
    today = str(date.today()).split('-')
    title = request.args.get("send_title")
    driver = webdriver.Chrome()

    for year in range(int(today[0]),2021,-1):

        for month in range(int(today[1]),0,-1):
            if len(str(month)) < 2 :
                month = "0" + str(month)

            for day in range(int(today[2]),0,-1):
                if len(str(day)) < 2 :
                    day = "0" + str(day)

            ######################### get all links  ######################################
                driver.get(f"https://medium.com/tag/{title}/archive/{year}/{month}/{day}")
                main = driver.find_element(By.TAG_NAME, "body")

                articles = main.find_elements(By.CLASS_NAME, "streamItem--postPreview")

                for article in articles:
                    titles = article.find_element(By.TAG_NAME, "h3")
                    print(titles.text)
                    link = article.find_elements(By.TAG_NAME, 'a')[3]
                    link_url = link.get_attribute("href")  
                    with open("./New_links.txt" , 'a') as file :
                        file.write(f"{titles.text}==={link_url}\n")
            #######################################################################
            today[2] = "30"
        today[1] = "12"
        

            
    return render_template('send_eamil.html')
            

@app.route('/send_email')
def send_email():
    send_email_for_login()
    return redirect(url_for('ok'))

@app.route('/ok')
def ok():
    return render_template("ok.html")

@app.route('/crateing_articles')
def creaing_files():
    email = read_email_for_login()
    link = regex_and_find_link(email)
    ############################# add for test ###############################
    print(f"this is link === {link}")
    input()
    ##########################################################################
    driver = webdriver.Chrome()
    driver.get(link)

    with open('./New_links.txt' , 'r') as file:
        all_text = file.readlines()
        for text in all_text:
            val = text.split("===")    
                
            url = val[1]
            file_name = val[0]
            
            driver.execute_script("setTimeout(6000);window.stop();")
            driver.get(url)
            
            # Find the element and get its text content
            element = driver.find_element(By.TAG_NAME , "article")
            text = element.text
            with open(f'../articles/{file_name}.txt' , 'a') as f :
                f.write(text)
    return render_template("tick.html")




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


