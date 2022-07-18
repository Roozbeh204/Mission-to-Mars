#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from bs4 import BeautifulSoup as soup

# selenium 4
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

import splinter
from splinter import Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser         = Browser('chrome', **executable_path, headless=False)

import sys
print(f"{'Python':<20}: {sys.version}")
print(f"{'':<20}: {sys.version_info}")
# print(f"{'BeautifulSoup':<20}: {soup.__version__}")
print(f"{'Selenium':<20}: {selenium.__version__}")
print(f"{'Splinter':<20}: {splinter.__version__}")
print(f"{'Webdriver Manager':<20}: {webdriver_manager.__version__}")


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


# !pip install lxml
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


browser.quit()

