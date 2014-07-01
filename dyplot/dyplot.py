import datetime as dt
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
        if type(self.x[0]) == dt.datetime:
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
        for l in csv_series:
            lines.append(l)
        with open(csv_file, 'w') as fp:
            cw = csv.writer(fp, lineterminator='\n', delimiter=',', quoting = csv.QUOTE_NONE)
            for line in lines:
                cw.writerow(line)
        snames = self.series.keys()
        if type(snames[0]) == type({}):
            max_value = max(self.snames[0].mseries.max(),self.snames[0].lseries.max(),self.snames[0].hseries.max())
            min_value = min(self.snames[0].mseries.min(),self.snames[0].lseries.min(),self.snames[0].hseries.min())
        else:
            max_value = self.snames[0].max()
            min_value = self.snames[0].min()
        snames.remove(snames[0])
        for n in snames:
            if type(names[n]) == type({}):
                tmax = max(self.names[n].mseries.max(),self.names[n].lseries.max(),self.names[n].hseries.max())
                tmin = min(self.names[n].mseries.min(),self.names[n].lseries.min(),self.names[n].hseries.min())
            else:
                tmax = self.names[n].max()
                tmin = self.names[n].min()
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
        div += '  valueRange: [' + min_value + ',' + max_value + '],\n'
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
