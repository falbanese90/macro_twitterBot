import tweepy
from config import twitter, twitter_pass, twitter_access, twitter_secret
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def scrape():
    # Allows selenium to run directly in incognito mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('headless')
    # Selenium runs your browser and opens webpage
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    driver.get('https://tradingeconomics.com/calendar')
    # Sets java script variables and executes them on page
    calendar_range = 'setCalendarRange("3")'
    calendar_importance = 'setCalendarImportance("3")'
    driver.execute_script(calendar_range)
    driver.execute_script(calendar_importance)
    # Extracts source code and makes a Beautiful Soup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # Extracts all inner html text of headline info
    calendar_events = soup.find_all('a', class_='calendar-event')
    # Extract list of countries so we can know where headline event takes place
    countries = soup.find_all('td', class_='calendar-iso')
    country_list = []
    for n in countries:
        country_list.append(n.get_text())
    # writes a text file of list of macro-  economic events
    # taking place this week
    countries = soup.find_all('td', class_='calendar-iso')
    with open('events.txt', 'w') as events:
        x = 0
        for n in calendar_events:
            events.write(country_list[x] + " - " + n.get_text() + '\n')
            x += 1
    # Selenium closes browser instance
    driver.quit()


def tweet():
    # Activates twitter api with OAuth
    auth = tweepy.OAuthHandler(twitter, twitter_pass)
    auth.set_access_token(twitter_access, twitter_secret)
    api = tweepy.API(auth)
    # Tweets the written file
    with open('events.txt', 'r') as events:
        api.update_status('Major Macro Events for this week:\n\n' + events.read())


scrape()
time.sleep(10)
tweet()
