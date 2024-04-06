from bs4 import BeautifulSoup
import requests
import csv
# import time
# import pandas as pd




#header for request
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Sec-Ch-Ua":'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123" '           }
url = "https://www.amazon.in/s?k=gaming+monitor&ref=nb_sb_noss"


# Number of attempts to make
max_attempts = 5

for attempt in range(max_attempts):
    # Send a GET request to the URL
    page = requests.get(url, headers=HEADERS)
    
    # Create a BeautifulSoup object
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    
    # Find the title
    title = soup2.find("span", class_="a-size-medium a-color-base a-text-normal")
    
    # Find the span element containing the price
    price_span = soup2.find("span", class_="a-price-whole")
    
    # Check if both title and price are found
    if title and price_span:
        title_text = title.get_text().strip()
        price_text = price_span.get_text().strip()
        print(f"Product: {title_text}\nPrice: {price_text}")
        break
    else:
        print(f"Attempt {attempt+1}/{max_attempts} failed. Retrying...")
else:
    print("Maximum retry attempts reached. Data could not be retrieved.")


# page = requests.get(url,headers=HEADERS)


# soup1 = BeautifulSoup(page.content,"html.parser")
# soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

# title = soup2.find(id='productTitle').get_text().strip()
# # Find the span element containing the price
# price_span = soup2.find("span", class_="a-price-whole")

# # Extract the price text
# price = price_span.get_text().strip() if price_span else "Price not found"



# newline = '\n'

# print(f"product:{title} {newline} price:{price} ")











# comments = []

# def scrape_youtube_comments(video_url):
#     response = requests.get(video_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Find all comment elements
#     comment_elements = soup.find_all('ytd-comment-renderer')

    
#     for comment in comment_elements:
#         username = comment.find('a', class_='yt-simple-endpoint').text
#         comment_text = comment.find('yt-formatted-string', id='content-text').text
        
#         comments.append({'username': username, 'comment': comment_text})
    
#     return comments


# video_url = "https://www.youtube.com/watch?v=IIat8oxEIbE"
# comments = scrape_youtube_comments(video_url)
# for comment in comments:
#     print(comment['username'], '-', comment['comment'])