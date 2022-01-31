from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from gtts import gTTS
import os

language = "en"
website = "https://www.royalroad.com/fiction/48065/improvisation-and-magic-dont-mix-a-progression/chapter/777168/1-endings-and-beginnings"

PATH = "F:\chromedriver.exe"

def get_content_selenium(link):
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    print(driver.title)
    body = driver.find_element_by_class_name("chapter-content")
    print(body.text)
    driver.quit()
    return body.text

def get_content_bs4(link):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(link,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    chapter_content = ''
    for data in soup.findAll('div',{'class':'chapter-content'}):
        for item in data.find_all('p'):
            chapter_content = chapter_content + item.text
        print(chapter_content)
    return chapter_content


content = get_content_bs4(website)

#get mp3 from gtts

output = gTTS(text=content, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")

# Get all the elements available with tag name 'p'
#elements = body.find_elements(By.TAG_NAME, 'p')

#for e in elements:
    #print(e.text)