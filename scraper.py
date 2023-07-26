from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import mysql.connector


def scroll_to_end(wd):
    wd.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
    time.sleep(3)

def find_elements(wd,selector,attribute=""):
    web_elements = wd.find_elements(By.CSS_SELECTOR,selector)
    extracted_attributes = []
    if attribute == 'href' or attribute == 'src':

        for element in web_elements:
            extracted_attribute = element.get_attribute(attribute)
            extracted_attributes.append(extracted_attribute)
    elif attribute == 'text':
        for element in web_elements:
            extracted_attribute = element.text
            extracted_attributes.append(extracted_attribute)
    else:
        for element in web_elements:
            return extracted_attributes.append(element)
    return extracted_attributes

def extractVideoDetails(url):

    with webdriver.Chrome() as wd:
        wd.get(url)
        time.sleep(10)
        wd.execute_script('window.scrollTo(0,300)')
        time.sleep(10)



        videoDetails=[]
        title = find_elements(wd,'#title h1','text')[0]
        likes = find_elements(wd, '#segmented-like-button', 'text')[0]
        commentCount = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".count-text"))).text.split(' ')[0]
        videoDetails.append(title)
        videoDetails.append(likes)
        videoDetails.append(commentCount)





        prev_length=0
        while True:
            scroll_to_end(wd)
            # Entire comment and commentor's name
            comments = find_elements(wd, '#comment-content', 'text')
            commentorName = find_elements(wd, '#author-text', 'text')
            # Checking if all the comments are extracted
            if prev_length == len(comments):
                break

            prev_length = len(comments)
        # Comments are appended in the list


    cmtList = []
    for comment_id in range(len(comments)):
        if comments[comment_id] == "":
            continue
        else:
            comments[comment_id] = [comments[comment_id], commentorName[comment_id]]
            cmtList.append(comments[comment_id])
        videoDetails.append(cmtList)
    return videoDetails