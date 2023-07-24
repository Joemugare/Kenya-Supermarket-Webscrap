#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# # Pull in data from website

# In[16]:


from bs4 import BeautifulSoup

# The provided HTML snippet
html = '<div data-testid="description-box" class="css-q7lfpb"><section class="css-168eikn"><div class="css-1khiat5"><div class="css-1bdwabt">More from  <a href="/mafken/en/JOGOO/c/55483" class="css-1nnke3o">JOGOO</a></div></div><h1 class="css-106scfp">Jogoo Maize Meal Fortified With Vitamins And Minerals 2kg</h1><div class="css-1kxxv3q">Pack size : 2kg</div><div class="css-1oh8fze"><h2 class="css-17ctnp">KES 210.00<span class="css-veux23">(Inc. VAT)</span></h2></div></section></div>'

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Extract the product name from the h1 element with class "css-106scfp"
product_name_element = soup.find("h1", class_="css-106scfp")

# Extract the product price from the h2 element with class "css-17ctnp"
price_element = soup.find("h2", class_="css-17ctnp")

# Extract the product name and price text if the elements are found
if product_name_element:
    product_name = product_name_element.get_text().strip()
else:
    product_name = "Product name not found on the page."

if price_element:
    price = price_element.get_text().strip()
else:
    price = "Price not found on the page."

# Print the extracted product name and price
print("Product Name:", product_name)
print("Product Price:", price)




# # Create a Timestamp for your output to track when data was collected

# In[17]:


import datetime

today = datetime.date.today()

print(today)


# # Create CSV and write headers and data into the file

# In[21]:


import csv 

# Assuming you have already extracted these values
title = "Jogoo Maize Meal Fortified With Vitamins And Minerals 2kg"
price = "KES 210.00(Inc. VAT)"
today = "2023-07-24"

header = ['Title', 'Price', 'Date']
data = [title, price, today]

# Specify the full path for the download location
download_location = r"C:\Users\Qunta\Desktop\PYTHON CODES\Carrefour.csv"

# Write the data to the CSV file
with open(download_location, 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

print("CSV file created at:", download_location)



# # Import the CSV file

# In[23]:


import pandas as pd

df = pd.read_csv('Carrefour.csv')


# In[24]:


df


# # Append data to the csv

# In[27]:


with open('Carrefour.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[28]:


df


# In[ ]:




