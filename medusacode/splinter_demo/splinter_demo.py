#!/usr/bin/env python
# coding:utf-8

from splinter import Browser

# Create a Browser instance (chrome, firefox, ...)
browser = Browser('chrome')

# Visit website
# (visit is a blocking operation:
#  it waits for page to load, then we can navigate, click on links, fill forms, etc. )
browser.visit('http://www.baidu.com')
print browser.url
print browser.title
print browser.html

# Input search text
browser.fill('wd', '12306')

# Press the search button
button = browser.find_by_id('su')
button.click()

# Interacting with elements in the page
# (the find_* method returns a list of all found elements)
# (If an element is not found, the find_* methods return an empty list.
#  But if you try to access an element in this list,
#  the method will raise splinter.exceptions.ElementDoesNotExist )

# [1] Get value of an element
content_left = browser.find_by_id('content_left')
print len(content_left)
print content_left[0].value

# [2] Clicking links
browser.click_link_by_partial_text(u'铁道部火车票网上订票唯一官网 - 铁路客户服务中心')

# Close the browser
import time
time.sleep(10)
browser.quit()
