from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from googletrans import Translator
from selenium.webdriver.common.keys import Keys
import smtplib 
import time
translator = Translator()
op = webdriver.ChromeOptions()
op.add_argument('headless')
qtd_of_articles = 0
counter = 63
#driver = webdriver.Chrome(executable_path=r'C:\\Users\\danil\\.spyder-py3\\chromedriver.exe', options=op)
driver = webdriver.Chrome(executable_path=r'C:\\Users\\danil\\.spyder-py3\\chromedriver.exe')
while (qtd_of_articles < 4):
    url = 'https://computersweden.idg.se/2.2683/1.7792' + str(counter)
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idgcp__section"]/div[2]/div/div/footer/button[2]'))).click()
    except:
        1==1
    
    orig_title = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="articlePage-1"]/div[1]/h1'))).text
    orig_article = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="articlePage-1"]/div[2]/div[1]/div[4]/div'))).text
    eng_title = translator.translate(orig_title)
    eng_article = translator.translate(orig_article)
    driver.get('https://app.writesonic.com/pt-pt/login')
    try:
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(Keys.CONTROL + "a")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(Keys.DELETE)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys('danilo.fe.antunes@gmail.com')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/form/div[2]/button[2]'))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/form/div[2]/input'))).send_keys('swedishpost')
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/main/form/div[3]/button[1]'))).click()
        time.sleep(10) 
        driver.get('https://app.writesonic.com/pt-pt/template/2e84a463-e998-4c60-bec7-08dab06915fb/chatsonic/202bcddc-c154-4baf-aad5-7d3d53dccde3')
    except:
        driver.get('https://app.writesonic.com/pt-pt/template/2e84a463-e998-4c60-bec7-08dab06915fb/chatsonic/202bcddc-c154-4baf-aad5-7d3d53dccde3')
        1==1
    try:    
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div/div/div[2]/button'))).click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-dialog-panel-:r2b:"]/div/div[1]/div[2]/button'))).click()
    except:
        1==1
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div/button'))).click()
    #WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scrollToBottom"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]'))).click()
    text_to_generate = 'Rephrase the given content in a professional way and enlarge the content to fit into 250 words while still keeping it focused and to the point, taking in consideration that we are currently living in 2023 : ' + eng_article.text.replace('\n', ' ').replace('-', ' ')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scrollToBottom"]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/textarea'))).send_keys(text_to_generate) 
    time.sleep(10)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div'))).click()
    time.sleep(20) 
    article = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/main/div/div/div[2]/div[2]/div/div[1]/div[2]/div'))).text.replace('\n', '\n\n').replace('\\t', '\t').replace('ä', 'a').replace('å', 'a').replace('ö', 'o').replace('Ö', 'O').replace('\\t', '\t') + '<p>Source: <a href="' + url + '">TN</a> </p>'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
        email_address = 'danilo.fe.antunes@gmail.com'
        email_password = 'xxxxx'
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs='lite452foku@post.wordpress.com', 
        msg="[title "+ eng_title.text  +" ]" + "[category Tech ] [tags featured]" + article)
    qtd_of_articles   = qtd_of_articles + 1
    counter = counter -4
    
        
        
