# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:18:40 2020

@author: Ben
"""

# -*- coding: utf-8 -*-
"""
Ben Xavier


README:
    Need to install selenium and beautifulsoup4
    Need to install Chromedriver, or another web-browser driver, link for chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
    Need to set correct path to web-driver
"""

import requests 
from bs4 import BeautifulSoup
import csv
import numpy as np
from sklearn.linear_model import LinearRegression 

import pandas



class AptListing:
    def __init__(self, name, address, price_list, bed_list, bath_list, sqr_ft_list):
        self.name = name
        self.address = address
        self.price_list = price_list
        self.bed_list = bed_list
        self.bath_list = bath_list
        self.sqr_ft_list = sqr_ft_list
        
    def print_to_console(self):
        print(self.name)
        print(self.address)
        print(self.price_list)
        print(self.bed_list)
        print(self.bath_list)
        print(self.sqr_ft_list)
        
    def print_to_csv(self):
        
        with open('apt_file.csv', mode='w') as apt_file:
            apt_writer = csv.writer(apt_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        apt_writer.writerow(['Name', 'Address', 'Price', 'Num Beds', 'Num Baths', 'Sqr footage'])
        apt_writer.writerow(['Erica Meyers', 'IT', 'March'])
    
    
        


def getAllAptURLs(urls): 
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    url_list = []
    for url in urls:
        url_list.append(url)
        page = requests.get(url, headers=headers,  timeout=5) 
        soup = BeautifulSoup(page.text, 'html.parser')
    
        num_pages = soup.find("span", class_= "pageRange")
    
        count = 1
        while(count < (num_pages.text[0]+1)):
            print("On page number " + count)
            new_url = URL + str(count)
            url_list.append(new_url)
            getAptLinks(new_url)
            count = count + 1 
            
    return url_list
    

def getAptLinks(url):
    print("getAptLinks Method Start")
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    page = requests.get(url, headers=headers,  timeout=5) 
    soup = BeautifulSoup(page.text, 'html.parser')

    results = soup.find_all("a", ["placardTitle"])
    #print(results)

    apts_list = []


    #print(test_results)
    for apt in results:
        apts_list.append(apt.get('href'))

    #title = apt.find('a', class_='placardTitle js-placardTitle  ')
    #print(title)
    print(apts_list)
    
#print(apt_pages)
    print("getAptLinks Method FINISHED")
    return apts_list

def getAptPages(apts_list):
    
    list_of_apts_buildings = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    for URL in apts_list:
        page = requests.get(URL, headers=headers,  timeout=5) 
        soup = BeautifulSoup(page.text, 'html.parser')
        list_of_apts_buildings.append(mineData(soup))
    return list_of_apts_buildings

#Takes a soup object with a single apartment complex     
#returns a AptListing object
def mineData(soup):
    
    property_name = soup.find("h1", class_="propertyName")
    print(property_name.text)
    
    address = soup.find("div", class_="propertyAddress")
    print(address.text)
    
    
    bed_room_values = soup.find_all("td", class_="beds")
    #print(bed_room_values)
    
    bath_room_values = soup.find_all("td", class_="baths")
    #for bath in bath_room_values:
        #print(bath.text[0])
        #print(bath.text[len(bath.text) - len(bath.text.lstrip())])
    
    square_foot_values = soup.find_all("td", class_="sqft")
    #print(square_foot_values)
    
    rent_values = soup.find_all("td", class_="rent")
    #print(rent_values)
    
    new_listing = AptListing(property_name, address, rent_values, bed_room_values, bath_room_values, square_foot_values)
    
    
    
    return new_listing
    
#def csvWriter(apt_object):
#    with open('apts.csv','wb') as csvfile:
#        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#        writer
        
    

URL = "https://www.apartments.com/del-mar-ca/"

getAptPages(getAptLinks(URL))