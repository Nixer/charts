import sqlite3
from open_charts_json import open_chart

us_chart = open_chart("us_charts.json")
uk_chart = open_chart("uk_charts.json")

conn = sqlite3.connect("webapp.db")
c = conn.cursor()

# for row in c.execute("PRAGMA table_info('track')").fetchall():
#     print(row)
#
# for row in c.execute("PRAGMA table_info('us_chart')").fetchall():
#     print(row)


def delete_data():
    c.execute("DELETE FROM track")
    c.execute("DELETE FROM us_chart")
    conn.commit()
    c.close()
    conn.close()


def add_json_chart_to_db(file):
    if "us" in file:
        chart_db = "us_chart"
    elif "uk" in file:
        chart_db = "uk_chart"
    else:
        print("Wrong file name!")
    chart = open_chart(file)
    for date in chart.keys():
        for track in chart[date]:
            c.execute("SELECT id FROM track WHERE title = ? AND artist = ?",
                      (track['title'], track['artist']))
            data = c.fetchone()
            if data is None:
                c.execute("INSERT INTO track (title, artist) VALUES (?,?)",
                          (track['title'], track['artist']))
                c.execute(f"INSERT INTO {chart_db} (track_id, date, rank) VALUES (?,?,?)",
                          (c.lastrowid, date, track['rank']))
            else:
                c.execute(f"SELECT id FROM {chart_db} WHERE date = ? AND rank = ?",
                          (date, track['rank']))
                data_chart = c.fetchone()
                if data_chart is None:
                    c.execute(f"INSERT INTO {chart_db} (track_id, date, rank) VALUES (?,?,?)",
                              (data[0], date, track['rank']))
                else:
                    pass
        conn.commit()

    c.close()
    conn.close()


def compare_json():
    for date in uk_chart.keys():
        print(f"\nChart for {date}:")
        for track in us_chart[date]:
            print(f"{track['rank']}. {track['artist']} - '{track['title']}'")


def compare_db():
    c.execute("SELECT * FROM us_chart")
    data = c.fetchall()
    for rank in data:
        c.execute(f"SELECT title, artist FROM track WHERE id = {rank[1]}")
        data = c.fetchone()
        print(f"{rank[3]}. {data[1]} - '{data[0]}' date: {rank[2]}")


# delete_data()
# compare_json()
# compare_db()
add_json_chart_to_db("us_charts.json")
