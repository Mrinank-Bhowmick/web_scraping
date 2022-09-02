from selenium.webdriver.firefox.service import Service
from selenium import webdriver

service=Service(r'C:\Users\bhowm\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')

driver=webdriver.Firefox(service=service)
driver.get('https://www.google.com/')
