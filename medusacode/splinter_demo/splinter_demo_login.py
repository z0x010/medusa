#!/usr/bin/env python
# coding:utf-8

from splinter import Browser

# Create a Browser instance (chrome, firefox, ...)
browser = Browser('chrome')

# Visit website
# (visit is a blocking operation:
#  it waits for page to load, then we can navigate, click on links, fill forms, etc. )
browser.visit('https://passport.baidu.com/v2/?login')
# print browser.url
# print browser.title
# print browser.html

# cookies before login
cookies_anonymous = browser.cookies.all()

# login Baidu
input_username = browser.find_by_name('userName')
input_password = browser.find_by_name('password')
input_button = browser.find_by_id('TANGRAM__PSP_3__submit')
input_username[0].fill('XXXXXX')
input_password[0].fill('XXXXXX')
input_button.click()

# cookies after login
cookies_login = browser.cookies.all()

print cookies_anonymous
# {
#   u'BAIDUID': u'1F6B67110DBC1C15487C450AA79B9905:FG=1',
#   u'Hm_lpvt_90056b3f84f90da57dc0f40150f005d5': u'1449221366',
#   u'Hm_lvt_90056b3f84f90da57dc0f40150f005d5': u'1449221366',
#   u'UBI': u'fi_PncwhpxZ%7ETaJc4nmK5Okozi7BKRvmARG',
#   u'HOSUPPORT': u'1'
# }
print cookies_login
# {
#   u'BAIDUID': u'1F6B67110DBC1C15487C450AA79B9905:FG=1',
#   u'Hm_lpvt_90056b3f84f90da57dc0f40150f005d5': u'1449221366',
#   u'Hm_lvt_90056b3f84f90da57dc0f40150f005d5': u'1449221366',
#   u'UBI': u'fi_PncwhpxZ%7ETaKASA33VG5tM3oVFY4p8wywUXlLt4vQrPpJQzzJFRUZHVgcQ4%7EStIC5Jq5fQVaqL9Y7wGt',
#   u'HOSUPPORT': u'1'
# }

# Close the browser
import time
time.sleep(10)
browser.quit()
