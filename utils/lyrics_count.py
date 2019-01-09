from PyLyrics import *
import re
import sqlite3

conn = sqlite3.connect("webapp.db")
c = conn.cursor()

# current_artist = "Stan Freberg"
# current_song = "Green Chri$tma$"
# lyrics = PyLyrics.getLyrics(current_artist, current_song)
# unique_words = set(re.findall(r"[\w']+", lyrics))
# print(lyrics)
# print(unique_words)
# print(len(unique_words))

c.execute('SELECT * FROM track WHERE id > 10000')
tracks = {}
for row in c:
    try:
        print(row)
        lyrics = PyLyrics.getLyrics(row[2], row[1])
        unique_words = set(re.findall(r"[\w']+", lyrics))
        print(len(unique_words))
        tracks[row[0]] = len(unique_words)
    except ValueError:
        pass


for id, words in tracks.items():
    c.execute(f"UPDATE track SET words = {words} WHERE id = {id}")
    conn.commit()

# conn.commit()
c.close()
conn.close()
