#!/usr/bin/env python3


## GOOGLE FINANCE STOCK DATA SCRAPER

# Notes: 1. You'll need to have the 'requests' module installed for this to work.
#        2. This is coded in Python 3.5.5... It may not work with earlier versions of Python. 
from lxml import html

import requests
import sys # Sys Module lets us interact with the machine we're on.

baseURL = 'https://www.google.com/finance?q=NYSE%3A' # You can grab any URL you want, just look for the commonly shared part of the url and then loop through the 'changing' part.
stocksOfInterest = ["QIHU","BX","AAPL"] # A list of the stocks whose wanted to see data
for i in range(1,len(stocksOfInterest)+1): # Starting at 1 and going for the length of the list of stocks to look at, execute the following:
      global stocksOfInterest # "global" tells python that this variable is the same one we declared prior to the 'for' function (see "Scoping Rules" for more info).
      global baseURL # ibid.
      stockURL = baseURL+stocksOfInterest[i-1] # concatenate the unchanging part of the URL plus the i-1 index of the lookup list (remember, lists/vectors are "0" based).
      page = requests.get(stockURL) # Using the 'requests' module, grab the html content of our webpage of interst.
      tree = html.fromstring(page.content) # Parse the html doc into an html tree (a logical form that you can work with).
      info = tree.xpath('//td[@class="key"]/text()') # using an XML XPATH, define the nodes for which you want to see the data (XML is a whole 'nother thing.  Google it for questions!).
      value = tree.xpath('//td[@class="val"]/text()') # ibid

      for j in range(1,len(info)): # This is a for-loop nested inside of the main for-loop.  It loops through each html tree xpath and prints out the node name and value.
      
            if j==1: # Print the ticker of the stock only if it's the 1st loop run.  Then, for all j, print the key-value pairs from our html trees.
                  print(stocksOfInterest[i-1], price)
            print(info[j-1],'Value:',value[j-1])

# That's it!


