#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:19:13 2018

@author: rohit
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://wwww.facebook.com')
driver.implicitly_wait(3)
driver.execute_script("window.open('http://www.twitter.com','new window')")