import pandas
import csv
import json
class Dyplot():
    def __init__(self, x, xname):
        self.x = x
        self.xname = xname
        self.series = {}
        self.annotations = []
        self.option = {}
        self.option["legend"] = 'always'
        self.option["showRoller"] = True
        self.option["customBars"] = True
        self.option["title"] = ""
        self.option["ylabel"] = "Y Values"
    def plot(self, name, mseries, lseries = None, hseries = None):
        if type(lseries) == type(None):
            self.series[name] = mseries
        else:
            self.series[name] = {}
            self.series[name]['l'] = lseries 
            self.series[name]['m'] = mseries 
            self.series[name]['h'] = hseries 
    def annotate(self, series, x, shortText, text=""):
        a = {}
        a["series"] = series
        a["shortText"] = shortText
        a["x"] = x
        a["text"] = text
        self.annotations.append(a)
    def set_options(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.option[key] = value
    def savefig(self, csv_file="dyplot.csv", div_id="dyplot", js_vid="g", dt_fmt="%Y-%m-%d", \
        html_file=None, width="1024px", height="600px"):
        csv_series = []
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
            if max_value > 0:
                max_value *= 1.1
            else:
                max_value *= 0.9
            if min_value > 0:
                min_value *= 0.9
            else:
                min_value *= 1.1
        self.set_options(valueRange=[min_value,max_value])
        div = '<div id="' + div_id + '" style="width:'+ width + '; height:' + height + ';"></div>\n'
        div += '<script type="text/javascript">\n'
        div += js_vid + ' = new Dygraph(\n'
        div += '    document.getElementById("' + div_id + '"),\n'
        div += '    "' + csv_file + '", // path to CSV file\n'
        div += json.dumps(self.option)
        div += '  );\n'
        div += '  ' + js_vid + '.ready(function() {\n'
        div += '    ' + js_vid + '.setAnnotations('
        div += json.dumps(self.annotations)
        div += '    );\n'
        div += '  });\n'
        div += '</script>\n'
        if type(html_file) != type(None):
            self.save_html(html_file, div)
        return div
    def save_html(self, html_file, div):
        header = """<html>
<head>
<script type="text/javascript"
  src="/js/dygraph-combined.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)

