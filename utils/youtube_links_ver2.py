# import urllib.request
# from bs4 import BeautifulSoup
#
# textToSearch = 'depeche+mode+personal+jesus'
# query = urllib.parse.quote(textToSearch)
# url = "https://www.youtube.com/results?search_query=" + query
# response = urllib.request.urlopen(url)
# html = response.read()
# soup = BeautifulSoup(html, 'html.parser')
# for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
#     print('https://www.youtube.com' + vid['href'])

import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query": input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])
