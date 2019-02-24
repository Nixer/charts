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
import sqlite3
import urllib.request
import urllib.parse
import re

conn = sqlite3.connect("webapp.db")
c = conn.cursor()


def get_yt_link(track):
    try:
        query = track + " (official video)"
        query_string = "http://www.youtube.com/results?" + urllib.parse.urlencode({"search_query": query})
        req = urllib.request.Request(
            query_string,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
            }
        )
        html_content = urllib.request.urlopen(req)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        yt_link = "http://www.youtube.com/watch?v=" + search_results[0]
        print(yt_link)
    except (urllib.error.HTTPError, ConnectionResetError, urllib.error.URLError):
        return None
    return yt_link


# c.execute('SELECT title, artist FROM track WHERE id > 64735')

for i in range(306, 10000):
    c.execute(f'SELECT title, artist FROM track WHERE id = {i}')
    tr = c.fetchone()
    print(f"{tr[1]} - {tr[0]}")
    yt_link = get_yt_link(f"{tr[1]} - {tr[0]}")
    if yt_link is not None:
        c.execute(f"UPDATE track SET youtube_link = '{str(yt_link)}' WHERE id = {i}")
    else:
        pass
    conn.commit()

c.close()
conn.close()

