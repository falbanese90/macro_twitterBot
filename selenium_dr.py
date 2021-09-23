from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def fetch_events():
    """Allows selenium to run directly in incognito mode
    Selenium runs your browser and opens webpage
    Sets java script variables and executes them on page
    Extracts source code and makes a Beautiful Soup object
    writes a text file of list of macro-economic events taking place this week
    Selenium closes browser instance"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(2)
    
    driver.get('https://tradingeconomics.com/calendar')
    calendar_range = 'setCalendarRange("3")'
    calendar_importance = 'setCalendarImportance("3")'
    driver.execute_script(calendar_range)
    driver.execute_script(calendar_importance)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    calendar_events = soup.find_all('a', class_='calendar-event')

    with open('events.txt', 'w') as events:
        for n in calendar_events:
            events.write(n.get_text() + '\n')
    driver.quit()
