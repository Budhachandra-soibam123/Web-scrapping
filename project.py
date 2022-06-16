import csv
import csv
import csv
from distutils.filelist import findall
from lib2to3.pgen2 import driver
from lib2to3.pytree import _Results
from re import template
from unittest import result
from bs4 import BeautifulSoup
from selenium import webdriver
driver= webdriver.Chrome()
url= 'https://www.amazon.in/'
driver.get(url)
def get_url(search_term):
    template='https://www.amazon.in/s?k={}&crid=3TZIQ5GZA94FY&sprefix=%2Caps%2C209&ref=nb_sb_ss_recent_1_0_recent'
    search_term= search_term.replace(' ',('+'))
    return template.format(search_term)
url= get_url('ultrawide monitor')
print(url)
driver.get(url)
soup= BeautifulSoup(driver.page_source,'html.parser')
result= soup.find_all,('div', {'data-component-type': 's-search-result'})
len(result)