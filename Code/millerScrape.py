
'''
Script written to scrape speech transcripts from Miller Center repository

HTML notes


view-source:https://millercenter.org/the-presidency/presidential-speeches

- NAMES

<form class="views-exposed-form bef-exposed-form" data-drupal-selector="views-exposed-form-presidential-speech-presidential-speech-view-block" action="/the-presidency/presidential-speeches" method="get" id="views-exposed-form-presidential-speech-presidential-speech-view-block" accept-charset="UTF-8">
  <fieldset data-drupal-selector="edit-field-president-target-id" id="edit-field-president-target-id--wrapper" class="fieldgroup form-composite js-form-item form-item js-form-wrapper form-wrapper">
      <legend>
    <span class="fieldset-legend">President</span>
  </legend>
  <div class="fieldset-wrapper">
            <div id="edit-field-president-target-id" class="form-checkboxes"><div class="form-checkboxes">
                  <div class="js-form-item form-item js-form-type-checkbox form-item-field-president-target-id-44 js-form-item-field-president-target-id-44">
        <input data-drupal-selector="edit-field-president-target-id-44" type="checkbox" id="edit-field-president-target-id-44" name="field_president_target_id[44]" value="44" class="form-checkbox" />

        <label for="edit-field-president-target-id-44" class="option">George Washington</label>
      </div>

                    <div class="js-form-item form-item js-form-type-checkbox form-item-field-president-target-id-45 js-form-item-field-president-target-id-45">
        <input data-drupal-selector="edit-field-president-target-id-45" type="checkbox" id="edit-field-president-target-id-45" name="field_president_target_id[45]" value="45" class="form-checkbox" />

        <label for="edit-field-president-target-id-45" class="option">John Adams</label>
      </div>


      

- SPEECHES

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


'''

import requests
from bs4 import BeautifulSoup

#site of list of all president names, need to a
url = https://millercenter.org/the-presidency/presidential-speeches
page = 