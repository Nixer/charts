import billboard


def billboard_charts(date):
    """Return dictionary with Billboard chart on particular date."""
    chart_dic = {date: {}}
    chart = billboard.ChartData('hot-100', date=date)
    for i in range(len(chart)):
        chart_dic[date][i+1] = [chart[i].title, chart[i].artist]
    return chart_dic


print(billboard_charts("2018-10-12"))
