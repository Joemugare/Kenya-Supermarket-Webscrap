#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Store': ['Naivas', 'Carrefour'],
    'Title': ['Jogoo Maize Meal 2Kg', 'Jogoo Maize Meal Fortified With Vitamins And Minerals 2kg'],
    'Price': ['KES 235.00(Inc. VAT)', 'KES 210.00(Inc. VAT)'],
    'Date': ['7/24/2023', '7/24/2023']
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Extract numeric price from the 'Price' column
df['Price'] = df['Price'].str.extract(r'(\d+\.\d+)').astype(float)

# Define custom colors for the bars
colors = ['blue', 'green']

# Create the bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Store'], df['Price'], color=colors)
plt.xlabel('Store Name')
plt.ylabel('Price (KES)')
plt.title('Price Comparison - Jogoo Maize Meal 2Kg')
plt.tight_layout()
plt.show()


# In[ ]:




