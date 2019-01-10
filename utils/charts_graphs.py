import pygal
from webapp.model import Track, UkChart, UsChart


def words_graph(us_chart, uk_chart):
    line_chart = pygal.Line()
    line_chart.x_labels = map(str, range(1, 101))

    def list_append(chart):
        wlist = []
        for c in chart:
            if c['words'] == None:
                wlist.append(None)
            else:
                wlist.append(c['words'])
        return wlist

    us_list = list_append(us_chart)
    uk_list = list_append(uk_chart)

    line_chart.add('Top 100 US', us_list)
    line_chart.add('Top 100 UK', uk_list)
    return line_chart.render_data_uri()
