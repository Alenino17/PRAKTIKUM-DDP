'''

from bs4 import BeautifulSoup4


html_soup = BeutifulSoup(open("index.html"), "html.parser")

judul = html_soup.find('p', class_='judul')
paragraf = html_soup.find('p', class_='paragraf')
judul_saja = html_soup.find('p', class_='judul').text


print(judul.prettify())
print(paragraf)