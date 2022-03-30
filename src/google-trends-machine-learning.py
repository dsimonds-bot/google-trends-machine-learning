#!/usr/bin/env python
# coding: utf-8

# # Google Trends Machine Learning
# Goal:
#    - Accept a user keyword for a trend they want to predict
#    - Take that keyword and pull time series data from google trends
#    - Run exploratory analysis on the time series data; check for trend, seasonality
#    - Create a forecast on the data so the user can make an estimated guess where market demand for the keyword, or product, will go

# In[1]:


# Package Imports
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.style as style
from pytrends.request import TrendReq
style.use('ggplot')

#test2


# ## Part 1: Data Import
# Goal:
# - Have the user define a keyword they want to study
# - Make the call to google trends api and pull time series data for the last 5 years on that keyword
# - Save the resultant data to a pandas dataframe for analysis

# In[2]:


# Setting up the trends API call; language english (en-US) and time 360 (US time zone)
pytrends = TrendReq(hl = 'en-US', tz = 360)

# Setting up the keyword --> * EDIT THIS *
kw = ['Alternative Investments']

# Grabbing the p12 months date range
endDate = datetime.date.today() - datetime.timedelta(1)
startDate = endDate - datetime.timedelta(365*5)
dateRange = str(startDate) + ' ' + str(endDate)

# Grabbing the data from api
pytrends.build_payload(kw_list= kw,
                       timeframe = dateRange,
                       geo = 'US'
                      )

# Saving the time series data
data = pytrends.interest_over_time()

# Checking results
data.head()


# ## Part 2: Exploratory Analysis
# Goal:
# - Visualze interest in alternative investments over time
# - Check data for trend, seasonality, stationary
# - Highlight anything that might impact modeling

# In[3]:


# Checking dataframe information
data.info()


# In[4]:


# Describing the dataframe
data.describe()


# In[6]:


# Plotting monthly moving average of interest over time
data['Alternative Investments'].rolling(4).mean().plot()


# In[2]:


get_ipython().system('jupyter nbconvert --to script google-trends-machine-learning.ipynb')

