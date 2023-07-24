#!/usr/bin/env python
# coding: utf-8

# In[26]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# # Pull in data from website

# In[27]:


from bs4 import BeautifulSoup

html_code = """
<a href="https://naivas.online/flour" class="item-name">
<span>FLOUR</span>
</a>
<h1 class="page-heading">Jogoo Maize Meal 2Kg</h1>
<span class="current-price">KES 235.00</span>
"""

# Parse the HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Extract product name
product_name = soup.h1.text.strip()

# Extract product price
product_price = soup.find('span', class_='current-price').text.strip()

# Print the results
print("Product Name:", product_name)
print("Product Price:", product_price)



# # Create a Timestamp for your output to track when data was collected

# In[28]:


import datetime

today = datetime.date.today()

print(today)


# # Create CSV and write headers and data into the file

# In[29]:


import csv 

# Assuming you have already extracted these values
title = "Jogoo Maize Meal 2Kg"
price = "KES 235.00(Inc. VAT)"
today = "2023-07-24"

header = ['Title', 'Price', 'Date']
data = [title, price, today]

# Specify the full path for the download location
download_location = r"C:\Users\Qunta\Desktop\PYTHON CODES\NaivasUnga.csv"

# Write the data to the CSV file
with open(download_location, 'w', newline='', encoding='UTF8') as f:
   writer = csv.writer(f)
   writer.writerow(header)
   writer.writerow(data)

print("CSV file created at:", download_location)



# # Import the CSV file

# In[30]:


import pandas as pd

df = pd.read_csv('NaivasUnga.csv')


# In[31]:


df


# In[ ]:




