import csv
class dyplot():
    def __init__(self, x, xname):
        self.x = x
        self.xname = xname
        self.series = {}
        self.annotations = []
    def plot(self, name, mseries, lseries = None, hseries = None):
        if type(lseries) == type(None):
            self.series[name] = mseries
        else:
            self.series[name] = {}
            self.series[name]['l'] = lseries 
            self.series[name]['m'] = mseries 
            self.series[name]['h'] = hseries 
    def annotate(self, a):
        for i in a:
            self.annotates.append(i) 
    def savefig(self, csv_file="dyplot.csv", div_id="dyplot", js_vid="g", dt_fmt="%Y-%m-%d", title=""):
        csv_series = []
        print type(self.x[0])
        if type(self.x[0]) == pandas.tslib.Timestamp:
            csv_series.append([])
            for e in self.x:
                csv_series[0].append(e.strftime(dt_fmt))
        else:
            csv_series.append(map(str, self.x))
        names = []
        names.append(self.xname)
        for s in self.series:
            if type(self.series[s]) == type({}):
                csv_series.append(self.series[s]['l'].map(str) + ";" + self.series[s]['m'].map(str) + ";" \
                    + self.series[s]['h'].map(str))
            else:
                csv_series.append(";" + self.series[s].map(str) + ";")
            names.append(s)
        lines = []
        lines.append(names)
        for i in range(len(csv_series[0])):
            l = []
            for series in csv_series:
                l.append(series[i])
            lines.append(l)
        with open(csv_file, 'w') as fp:
            cw = csv.writer(fp, lineterminator='\n', delimiter=',', quoting = csv.QUOTE_NONE)
            for line in lines:
                cw.writerow(line)
        snames = self.series.keys()
        n = snames[0]
        if type(self.series[n]) == type({}):
            max_value = max(self.series[n]["m"].max(),self.series[n]["l"].max(),self.series[n]["h"].max())
            min_value = min(self.series[n]["m"].min(),self.series[n]["l"].min(),self.series[n]["h"].min())
        else:
            max_value = self.series[n].max()
            min_value = self.series[n].min()
        snames.remove(n)
        for n in snames:
            if type(self.series[n]) == type({}):
                tmax = max(self.series[n]["m"].max(),self.series[n]["l"].max(),self.series[n]["h"].max())
                tmin = min(self.series[n]["m"].min(),self.series[n]["l"].min(),self.series[n]["h"].min())
            else:
                tmax = self.series[n].max()
                tmin = self.series[n].min()
            if tmax > max_value:
                max_value = tmax
            if tmin < min_value:
                min_value = tmin
        div = '<div id="' + div_id + '" style="width:1024px; height:600px;"></div>\n'
        div += '<script type="text/javascript">\n'
        div += js_vid + ' = new Dygraph(\n'
        div += '    document.getElementById("' + div_id + '"),\n'
        div += '    "' + csv_file + '", // path to CSV file\n'
        div += '  {\n'
        div += "  legend: 'always',"
        div += '  title: "' + title + '",\n'
        div += '  showRoller: true,\n'
        div += '  customBars: true,\n'
        div += '  valueRange: [' + str(min_value) + ',' + str(max_value) + '],\n'
        div += '  ylabel: "Ratio",\n'
        div += '  }\n'
        div += '  );\n'
        div += '  ' + js_vid + '.ready(function() {\n'
        div += '    ' + js_vid + '.setAnnotations([\n'
        for x in self.annotations:
            div += '    {\n'
            div += '      series: "' + x.series + '",\n'
            div += '      x: "' + x.x + '",\n'
            div += '      shortText: ' + x.shortText + ',\n'
            div += '      text: "' + x.text + '",\n'
            div += '    },\n'
        div += '    ]);\n'
        div += '  });\n'
        div += '</script>\n'
        return div
