import requests
import numpy as np
from bs4 import FILL_IN_THE_BLANK

# def scrapper(imdbId):
#     id = str(int(imdbId))
#     n_zeroes = 7 - len(id)
#     new_id = "0"*n_zeroes + id
#     URL = f"https://www.imdb.com/title/tt{new_id}/"
#     request_header = {'Content-Type': 'text/html; charset=UTF-8', 
#                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
#                       'Accept-Encoding': 'gzip, deflate, br'}
#     response = requests.FILL_IN_THE_BLANK(URL, headers=request_header)
#     soup = FILL_IN_THE_BLANK(response.text)
#     imdb_rating = soup.find('FILL_IN_THE_BLANK', attrs={'FILL_IN_THE_BLANK' : 'FILL_IN_THE_BLANK'})
#     return imdb_rating.text if imdb_rating else np.nan

def scraper(imdb_ids):
  data = []

  for id in imdb_ids:
    id_str = str(int(id)).zfill(7) 
    URL = f"https://www.imdb.com/title/tt{id_str}/reviews"
    request_header = {'Content-Type': 'text/html; charset=UTF-8', 
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
                      'Accept-Encoding': 'gzip, deflate, br'}
    response = requests.get(URL, headers=request_header)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      # Extract reviews
      reviews = soup.find_all('div', class_='text show-more__control')
      reviews_text = [review.get_text(strip=True) for review in reviews]

      #Collect the data
      data.append({'IMDB_ID':id, 'Reviews':reviews_text})
    else:
      print("Error occurred")
  return pd.DataFrame(data)

imdb_list = links['imdbId'].tolist()
reviews_df = scraper(imdb_list[:20])
print(reviews_df)
#print(imdb_list)