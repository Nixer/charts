from webapp.model import *


def get_records(date):
    years = [year for year in range(1958, 2020, 1)]
    days = [day for day in range(1, 32, 1)]
    current_top_us = []
    current_top_uk = []
    chart_for_date_uk = UkChart.query.filter_by(date=date).order_by(UkChart.rank).all()
    chart_for_date_us = UsChart.query.filter_by(date=date).order_by(UsChart.rank).all()
    for c in chart_for_date_uk:
        track = Track.query.get(c.track_id)
        current_top_uk.append({'title': track.title, 'artist': track.artist,
                               'rank': c.rank, 'words': track.words, 'ylink': track.youtube_link})
    for c in chart_for_date_us:
        track = Track.query.get(c.track_id)
        current_top_us.append({'title': track.title, 'artist': track.artist,
                               'rank': c.rank, 'words': track.words, 'ylink': track.youtube_link})
    return days, years, current_top_us, current_top_uk
