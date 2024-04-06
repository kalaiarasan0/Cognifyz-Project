#Data Scraping 
from bs4 import BeautifulSoup
import requests,openpyxl


excel = openpyxl.Workbook()

sheet = excel.active
sheet.title = "Movie List 250"
sheet.append(['Rank','Movie Name','Rating','Year','Duration'])

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "Accept-Language": "en-US,en;q=0.9", 
            }

try:

    url = requests.get("https://www.imdb.com/chart/top/",headers=HEADERS)

    soup1 = BeautifulSoup(url.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    movies_list = soup2.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base").find_all("li")

    for movie in movies_list:
        movie_rank = movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title").a.h3.text.strip().split('.')[0]
        movie_name_with_dot = movie.find('div', class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title").a.h3.text.strip()[3:]
        movie_name = movie_name_with_dot.lstrip('.')  # Remove the dot if present at the beginning
        movie_rating = movie.find('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.strip()[:3]
        release_year = movie.find('span', class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item").text.strip()
        movie_duration = None
        metadata_items = movie.find('div', class_="sc-b0691f29-7 hrgukm cli-title-metadata").find_all('span', class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item")
        for item in metadata_items:
            text = item.text.strip()
            if 'h' in text and 'm' in text:  # Check if the text contains both 'h' and 'm'
                movie_duration = text
            

        # print(movie_rank,movie_name,movie_rating,release_year,movie_duration)
        sheet.append([movie_rank,movie_name,movie_rating,release_year,movie_duration])
        

except Exception as e:
    print(e)

excel.save("Movie_List.xlsx")