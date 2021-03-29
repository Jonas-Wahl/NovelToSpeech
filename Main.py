from selenium import webdriver
from selenium.webdriver.common.by import By

from gtts import gTTS
import os

language = "en"


PATH = "F:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.royalroad.com/fiction/15935/there-is-no-epic-loot-here-only-puns/chapter/185054/1-smashing-start")

print(driver.title)

body = driver.find_element_by_class_name("chapter-content")

#print(body.text)
output = gTTS(text=body.text, lang=language, slow=False)
output.save("ch1.mp3")
os.system("start ch1.mp3")

# Get all the elements available with tag name 'p'
#elements = body.find_elements(By.TAG_NAME, 'p')

#for e in elements:
    #print(e.text)
    


driver.quit()
