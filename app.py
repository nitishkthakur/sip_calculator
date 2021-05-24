#import streamlit as st
#import pandas as pd
#import numpy as np
#import datetime

#st.write("Hello, Heroku! Test Deployment")
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import datetime
st.title('SIP Calculator')

# Start Date and Duration
date = st.sidebar.date_input('start date', datetime.date(2021,1,1))
st.write('Start Date: ', date)

no_of_years = st.sidebar.number_input(label = 'Number of Years', step  = 1.0, min_value = 0.0, 
max_value = 60.0, value = 10.0)
st.write('Number of Years: ', no_of_years)

rate_of_interest = st.sidebar.number_input(label = 'Annual Rate of Interest', step  = 0.5, 
min_value = 0.0, max_value = 25.0, value = 12.0)
st.write('Annual Rate of Interest: ', rate_of_interest)
st.write('Monthly Rate of Interest: ', rate_of_interest/12)

# Monthly Investment
monthly_amt = st.sidebar.number_input(label = 'Monthly Investment', step  = 500.0, 
min_value = 500.0, max_value = 75000.0, value = 2000.0)
st.write('Monthly Investment: ', monthly_amt)

# Execute Code
n_records = no_of_years * 12

# Calculate stuff
data = pd.DataFrame()
data['index'] = np.arange(n_records)
data['base_amt'] = monthly_amt
data['principal'] = monthly_amt
principal = monthly_amt

for index, row in data.iterrows():
    data.loc[index, 'principal'] = principal
    i = rate_of_interest/100/12
    amt = data.loc[index, 'principal']*(i)*((1 + i)/i)
    data.loc[index, 'amount'] = amt
    principal = amt + monthly_amt

date = pd.to_datetime(datetime.date(2021,1,1))
dates = pd.date_range(start = date, periods = n_records, freq = 'M')
#data['date'] = pd.to_datetime(dates, format = '%Y-%m ')
data['date'] = dates


data['month'] = data['date'].dt.month
data['quarter'] = data['date'].dt.quarter
data['year'] = data['date'].dt.year
data['Net Investment'] = np.arange(monthly_amt, monthly_amt+monthly_amt*n_records, monthly_amt)
disp = data[['date', 'Net Investment', 'amount']]
disp.columns = ['Date', 'Net Investment', 'Amount']
disp[['Net Investment', 'Amount']] = disp[['Net Investment', 'Amount']].astype(int)

ungp = disp.copy()
disp['Date'] = disp['Date'].dt.strftime('%Y-%m')
#disp['Date'] = disp['Date'].astype(str)
st.write(disp)

##### Plot
st.line_chart(ungp.set_index('Date'),)
