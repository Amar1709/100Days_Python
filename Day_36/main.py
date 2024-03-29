
# Day 36 - Stock Price Alerts Project
from twilio.rest import Client
import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY ="XPN4Q1V3F8CN2871"
News_API_key = "54e3c97cbc084b9094dfb6c919c6f396"

TWILIO_AUTH_TOKEN = "1f74552bfc62d3ef1bc35e9092be7ff0"
TWILIO_SID = "ACcb95af7d9fc479b49efe71b944e1c640"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]



stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT,params = stock_params)
data = response.json()["Time Series (Daily)"]
#print(data)
data_list = [value for (key, value) in data.items()]
yesterdays_closing_price = data_list[0]["4. close"]
print(yesterdays_closing_price) 



#2. - Get the day before yesterday's closing stock price
dayB4yesterday_closing_price = data_list[1]["4. close"]
print(dayB4yesterday_closing_price)

#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterdays_closing_price) - float(dayB4yesterday_closing_price))
print(difference)


#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (float(difference) / float(yesterdays_closing_price)) * 100
print(diff_percent)


#5. - If TODO4 percentage is greater than 5 then print("Get News").

# if diff_percent > 5:
#     print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percent > 5:
    news_params = {"qInTitle": COMPANY_NAME, "apiKey": News_API_key}
    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    
    articles = news_response.json()["articles"]
    #print(articles[0]["title"])




# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[0:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

# 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"Headline: {article['title']} \n Description: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body = article,
        from_= "+14129230688",
        to = "+919307274812"
        )

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

