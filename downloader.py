import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open browser
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--window-size=1920,1080")
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver = webdriver.Chrome(service=Service(executable_path='/root/chromedriver'), options=options)

# go to https://craftpix.net/
driver.get("https://craftpix.net/")

# click link "Hello. Sign in"
link_sign_in = driver.find_element(By.CLASS_NAME, "lr-singin")
link_sign_in.click()
driver.save_screenshot('after_click_form_signin.png')

# wait for sign in form to show
WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, "auth-form")))
driver.save_screenshot('after_login_form_visible.png')

# enter email and password, submit
email = "example@gmail.com"
password = "PassWord@123"

input_user_login = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/form/div[2]/input')))
input_user_login.send_keys(email)

input_user_pass = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/form/div[3]/input')
input_user_pass.send_keys(password)

input_user_pass.send_keys(Keys.RETURN)

# wait for sign in success, popup disapeared
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "auth-form")))
driver.save_screenshot('login_success.png')

article_links_filename = 'article-links.txt'
def get_article_links():

    # go to https://craftpix.net/freebies/
    driver.get("https://craftpix.net/freebies/")
    driver.save_screenshot('freebies.png')

    # for each article on first page, get link until page ends
    article_links = []
    while True:
        article_elements = driver.find_elements(By.XPATH, '//article/div/div/h2/a')
        
        with open(article_links_filename, 'a') as f:
            for element in article_elements:
                link = element.get_attribute('href')
                article_links.append(link)
                f.write(link + '\n')
        
        # loop to the last page
        # then we have list article link
        try:
            next_page_element = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/main/div/div/div/div/div/a[@class="nextpostslink"]')
        except selenium.common.exceptions.NoSuchElementException:
            break
        
        next_page_url = next_page_element.get_attribute('href')
        driver.get(next_page_url)
    
    return article_links

article_links = get_article_links()

# get article links from file
with open(article_links_filename, 'r') as f:
    article_links = [link.strip() for link in f.readlines()]
    print(article_links)

donwload_links_file = 'download-links.txt'
def get_download_links():
    # for each article link
    links_download = []
    for link in article_links:
        try:
            # go to article
            driver.get(link)

            # click download, wait 15s, get download link
            download_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/main/div/div/div/aside/div/div[3]/p[2]/a')))
            download_button.click()
            link_download = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div/main/div/article/div/div/div/div/p/a')))
            link_download = link_download.get_attribute('href')
            links_download.append(link_download)
            print(link_download)
        except Exception:
            continue

    with open(donwload_links_file, 'a') as f:
        for link in links_download:
            f.write(link + '\n')

    return links_download

download_links = get_download_links()

# get download links from file
with open(donwload_links_file, 'r') as f:
    donwload_links = [line.strip() for line in f.readlines()]

# for each link
for link in donwload_links:

    # download
    filename = link.split('/')[-1]
    res = requests.get(link)
    with open(filename, 'wb') as f:
        f.write(res.content)

driver.close()

# for each download link:
#   download
