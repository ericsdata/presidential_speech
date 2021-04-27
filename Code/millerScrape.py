
'''
Script written to scrape speech transcripts from Miller Center repository
Two step scrape

1. Page that hosts speeches contains links to each individual speech by each president. Selenium employed to deal with links hidden by infinite scrolling. 
Final product is link of links to scrape

2. Looping through links and scraping individual pages for Speech Name, President, Date and Content


'''
'''
HTML Samples
view-source:https://millercenter.org/the-presidency/presidential-speeches


- SPEECHES 

## Will need to engage this infinite scroll =>  https://medium.com/@harshvb7/scraping-from-a-website-with-infinite-scrolling-7e080ea8768e

  <div data-drupal-views-infinite-scroll-content-wrapper class="views-infinite-scroll-content-wrapper clearfix">    <div class="views-row"><div class="views-field views-field-title"><span class="field-content"><a href="/the-presidency/presidential-speeches/january-20-2021-inaugural-address" hreflang="en">January 20, 2021: Inaugural Address</a></span></div><div class="views-field views-field-presidential-media-icons"><span class="field-content"><section class="speech-icons-column">
            <span class="media-video">video icon</span>
                <span class="media-audio">audio icon</span>
                <span class="media-transcript">transcript icon</span>
    </section>
</span></div></div>
    <div class="views-row"><div class="views-field views-field-title"><span class="field-content"><a href="/the-presidency/presidential-speeches/january-19-2021-farewell-address" hreflang="en">January 19, 2021: Farewell Address</a></span></div><div class="views-field views-field-presidential-media-icons"><span class="field-content"><section class="speech-icons-column">
            <span class="media-video">video icon</span>
                <span class="media-audio">audio icon</span>
                <span class="media-transcript">transcript icon</span>
    </section>
</span></div></div>
    <div class="views-row"><div class="views-field views-field-title"><span class="field-content"><a href="/the-presidency/presidential-speeches/january-13-2021-statement-about-violence-capitol" hreflang="en">January 13, 2021: Statement about the Violence at the Capitol</a></span></div><div class="views-field views-field-presidential-media-icons"><span class="field-content"><section class="speech-icons-column">
            <span class="media-video">video icon</span>
                <span class="media-audio">audio icon</span>
                <span class="media-transcript">transcript icon</span>
    </section>
</span></div></div>
    <div class="views-row"><div class="views-field views-field-title"><span class="field-content"><a href="/the-presidency/presidential-speeches/january-7-2021-message-after-pro-trump-mob-overruns-us-capitol" hreflang="en">January 7, 2021: Message After Pro-Trump Mob Overruns US Capitol</a></span></div><div class="views-field views-field-presidential-media-icons"><span class="field-content"><section class="speech-icons-column">
            <span class="media-video">video icon</span>
                <span class="media-audio">audio icon</span>
                <span class="media-transcript">transcript icon</span>




view-sorce: /presidential-speeches/january-19-2021-farewell-address

pull meta data here

<div  class="about-this-episode">
    <h3>About this speech</h3>
      
<div  class="about-this-episode--inner">
      
            <p class="president-name">Donald Trump</p>
      
            <p class="episode-date">January 19, 2021</p>

TRANSCRIPT

'''

import requests
from bs4 import BeautifulSoup

import regex as re

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Url of page
### Speeches are hidden by an infitie scroll
url = "https://millercenter.org/the-presidency/presidential-speeches"

## Use seleium to open browser
#make browser
browser = webdriver.Chrome()
#fetch site
browser.get(url)
time.sleep(1)
## Get HTML body
elem = browser.find_element_by_tag_name("body")

## Set up
## Lets scroll 500 times down
no_pagedowns = 500

while no_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_pagedowns -= 1


## From above HTML sample, field content is target
speech_rows = browser.find_elements_by_class_name('field-content')

## Loop through and pull out html within field content tags
temp = []
for html in speech_rows:
    #extract string from html
    html_txt = html.get_attribute('innerHTML')
    # if match append matched group to list
    match_url = re.search('href="(.*)"', html_txt)
    match_sppech = re.search
    if match:
        temp.append(match.group(1))




url2 ="https://millercenter.org/views/ajax?_wrapper_format=drupal_ajax"

page = requests.get(url2)

soup = BeautifulSoup(page.content,'html.parser')

## Parse through HREF - append url to direct to each speech page
f = soup.findall(class_ = 'views-row')
