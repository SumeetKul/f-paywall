#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from argparse import ArgumentParser

# Get link from the command line argument
parser = ArgumentParser()
parser.add_argument("link",nargs=1)
args = parser.parse_args()

print(args.link[0])

options = Options()

prefs = {"profile.managed_default_content_settings.javascript" : 2}

# add prefs 
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-javascript")

# setup driver and keep running for an hour
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(args.link[0])
time.sleep(3600)

