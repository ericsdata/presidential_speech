
'''
Script written to scrape speech transcripts from Miller Center repository

HTML notes




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

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#site of list of all president names, need to a

## Selenium

url = "https://millercenter.org/the-presidency/presidential-speeches"



#make browser
browser = webdriver.Chrome()

browser.get(url)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")


## Lets scroll 500 times down
no_pagedowns = 500

while no_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_pagedowns -= 1


links = browser.find_elements_by_tag_name("a")
pp = browser.find_elements_by_class_name('field-content')

lt = browser.find_elements_by_link_text("presidential-speeches")



temp = []
for link in pp:
    temp.append(link.getAttribute('href'))




url2 ="https://millercenter.org/views/ajax?_wrapper_format=drupal_ajax"

page = requests.get(url2)

soup = BeautifulSoup(page.content,'html.parser')

## Parse through HREF - append url to direct to each speech page
f = soup.findall(class_ = 'views-row')
