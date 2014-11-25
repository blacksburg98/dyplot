import pandas
import csv
import json
class Dygraphs():
    def __init__(self, x, xname):
        self.x = x
        self.xname = xname
        self.series = {}
        self.annotations = []
        self.option = {}
        self.option["legend"] = 'always'
        self.option["showRoller"] = False
        self.option["customBars"] = True
        self.option["title"] = ""
        self.option["ylabel"] = "Y Values"
        self.option["series"] = {}
        self.option["axes"] = {}
        self.option["axes"]['x'] = {}
        self.option["axes"]['y'] = {}
        self.option["axes"]['y2'] = {}
        self.option["axes"]['y']['valueRange'] = []
        self.option["axes"]['y2']['valueRange'] = []
    def plot(self, series, mseries, lseries = None, hseries = None, **kwargs):
        if series not in self.option["series"]:
            self.option["series"][series] = {}
        self.option["series"][series]["axis"] = 'y'
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.option["series"][series][key] = value
        if type(lseries) == type(None):
            self.series[series] = mseries
        else:
            self.series[series] = {}
            self.series[series]['l'] = lseries 
            self.series[series]['m'] = mseries 
            self.series[series]['h'] = hseries 
    def annotate(self, series, x, shortText, text=""):
        a = {}
        a["series"] = series
        a["shortText"] = shortText
        a["x"] = x
        a["text"] = text
        self.annotations.append(a)
    def set_axis_options(self, axis, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.option['axes'][axis][key] = value
    def set_series_options(self, series, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.option['series'][series][key] = value
    def set_options(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self.option[key] = value
    def auto_range(self, axis="y"):
        snames = self.series.keys()
        anames = [x for x in snames if self.option["series"][x]["axis"] == axis] 
        if anames == []:
            return
        n = anames[0]
        if type(self.series[n]) == type({}):
            max_value = max(self.series[n]["m"].max(),self.series[n]["l"].max(),self.series[n]["h"].max())
            min_value = min(self.series[n]["m"].min(),self.series[n]["l"].min(),self.series[n]["h"].min())
        else:
            max_value = self.series[n].max()
            min_value = self.series[n].min()
        anames.remove(n)
        for n in anames:
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
        self.option['axes'][axis]['valueRange'] = [min_value, max_value]
    def save_csv(self, csv_file, dt_fmt):
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
    def savefig(self, csv_file="dyplot.csv", div_id="dyplot", js_vid="g", dt_fmt="%Y-%m-%d", \
        html_file=None, width="1024px", height="600px"):
        self.save_csv(csv_file, dt_fmt)
        if self.option['axes']['y']['valueRange'] == []:
            self.auto_range(axis='y')
        if self.option['axes']['y2']['valueRange'] == []:
            self.auto_range(axis='y2')
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

