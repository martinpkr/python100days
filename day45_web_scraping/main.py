from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
website_html = response.text
soup = BeautifulSoup(website_html,'html.parser')

movies = soup.find_all(name='h3',class_='title')

movies_titles = [movie.getText() for movie in movies]
for n in range(len(movies_titles) -1, 0, -1 ):
    #n - 1 because we want the last element in the list
    print(movies_titles[n - 1 ])