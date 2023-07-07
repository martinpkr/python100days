import os

import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_market_API_KEY = 'RMPO4M8YXN7QSJR2'
stock = os.environ.get("MARKET_KEY")
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'SHOP.TRT',
    'apikey': stock_market_API_KEY,
}

response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()

data = response.json()

now = dt.datetime.now()
date_now = str(now).split(' ')[0]
get_day = int(date_now.split('-')[2]) - 2
date = date_now.split('-')
year = date[0]
month = date[1]
day = get_day
string_for_key = f'{year}-{month}-{day}'

#TODO 2. - Get the day before yesterday's closing stock price

get_day_bfyesterday = int(date_now.split('-')[2]) - 3
year = date[0]
month = date[1]
string_for_key_bfyesterday = f'{year}-{month}-{get_day_bfyesterday}'

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
yesterday_close = data['Time Series (Daily)'][string_for_key]['4. close']
day_before_yesterday_close = data['Time Series (Daily)'][string_for_key_bfyesterday]['4. close']
increase = int

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

def find_percentige(original_number,increase):
    percentige = increase / float(original_number) * 100
    return percentige

if yesterday_close > day_before_yesterday_close:
    increase = float(yesterday_close) - float(day_before_yesterday_close)
    diff_in_percentige = find_percentige(yesterday_close,increase)
else:
    increase = float(day_before_yesterday_close) - float(yesterday_close)
    diff_in_percentige = find_percentige(day_before_yesterday_close, increase)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_params = {
    'q': 'shopify',
    'apiKey': '2eea8df593f74682bc322bb88aeb84f5',
    'sortBy': 'popularity',
}

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

response_for_news = requests.get(NEWS_ENDPOINT, params= news_params)
response_for_news.raise_for_status()

news_data = response_for_news.json()
article = news_data['articles'][0:2]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

articles = news_data['articles'][0:2]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

info_dump = [f'{article["title"]}\n{article["content"]}' for article in articles]
print(info_dump)
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

