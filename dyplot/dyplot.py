import datetime as dt
class dyplot():
    def __init__(x, xname):
        self.x = x
        self.xname = xname
        self.series = {}
    def plot(mseries, name, lseries = [], hseries = []):
        if lseries == []:
            self.series[name] = mseries
        else:
            self.series[name] = {}
            self.series[name]['l'] = lserie 
            self.series[name]['m'] = mserie 
            self.series[name]['h'] = hserie 
    def savefig(csv_file="dyplot.csv", div_name="dyplot", js_vname="g", dt_fmt="%Y-%m-%d"):
        csv_series = []
        if type(x[0]) == dt.datetime:
            csv_series.append([])
            for e in self.x:
                csv_series[0].append(e.strftime(dt_fmt))
        else:
            csv_series.append(map(str, self.x))
        names = []
        names.append(xname)
        for s in self.series:
            if type(self.series[s]) == type([]):
                csv_series.append(";" + total_nml.map(str) + ";")
            elif type(self.series[s]) == type({}):
                 csv_series.append(self.series['l'].map(str) + ";" + self.series['m'].map(str) + ";" \
                        + self.series['h'].map(str))
            names.append(s)
        lines = []
        lines.append([xname, "Russel 3000", tick, algo])
        for i in dygraph.index:
            l = []
            l.append(i.strftime("%Y-%m-%d"))
            l.append(market_dygraph[i])
            l.append(tick_dygraph[i])
            l.append(dygraph[i])
            lines.append(l)
        csv_file = tick + "_dygraph.csv"
        with open(csv_file, 'w') as fp:
            cw = csv.writer(fp, lineterminator='\n', delimiter=',', quoting = csv.QUOTE_NONE)
            for line in lines:
                cw.writerow(line)
