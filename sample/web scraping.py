import os
os.environ['PYPPETEER_DOWNLOAD_HOST'] = 'https://npm.taobao.org/mirrors'
os.environ['PYPPETEER_NO_SANDBOX'] = '1'  # Disable sandbox
os.environ['PYPPETEER_DOWNLOAD_PROGRESS'] = '1' #show download progress


from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

url = "https://www.youtube.com/watch?v=7hLRRDpPeXk&lc=Ugw1HatMwlN_xhCJL4t4AaABAg"

data = []

response = session.get(url)

# Render the JavaScript page
response.html.render(sleep=3, timeout=100, keep_page=True, scrolldown=20)

# Find data elements
containers = response.html.find('ytd-comment-thread-renderer')

# Scraping all data
for container in containers:
    user_name = container.find('a.yt-simple-endpoint.style-scope.yt-formatted-string', first=True).text
    user_url = 'https://www.youtube.com' + container.find('a.yt-simple-endpoint.style-scope.yt-formatted-string')[0].attrs['href']
    comment = container.find('yt-formatted-string#content-text', first=True).text

    # Append all data
    data.append([user_name, user_url, comment])

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['User Name', 'User Url', 'Comment'])
df.to_csv('youtube_dataset.csv', index=False)
