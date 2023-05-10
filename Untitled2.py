#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriverchrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome(chrome_options=options)

# set the path you want to go
path = "https://www.facebook.com/"
chrome.get(path)

