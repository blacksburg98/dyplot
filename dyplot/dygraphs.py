import pandas
import csv
import json
class Dygraphs():
    """ matplotlib-like plot functions for dygraphs.js and c3.js.
        Dygraph.py makes it easier to integrate dygraphs.js into webpage.
        Pleas see dygaphs.com for detail.
    """
    def __init__(self, x, xname):
        """ Initialization

            :param x: x-axis. 
            :type x: index list from pandas.
            :param xname: x-axis name.
            :type xname: string
        """
        self.x = x
        self.xname = xname
        self.series = {}
        self.annotations = []
        self.candle = False
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
        """ 
            the function to plot the series.
            If lseries is specified, dygraphs will shade the space between the main series and the low series.
            If hseries is specified, dygraphs will shade the space between the main series and the high series.

            :param series: Series name
            :type series: string
            :param mseries: The main series. 
            :type mseries: pandas series.
            :param lseries: The low series. 
            :type lseries: pandas series.
            :param hseries: The high series. 
            :type hseries: pandas series.
        """
        if series not in self.option["series"]:
            self.option["series"][series] = {}
        self.option["series"][series]["axis"] = 'y'
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option["series"][series][key] = value
        if type(lseries) == type(None):
            self.series[series] = mseries
        else:
            self.series[series] = {}
            self.series[series]['l'] = lseries 
            self.series[series]['m'] = mseries 
            self.series[series]['h'] = hseries 
    def candleplot(self, open, close, high, low, **kwargs):

        """ Candle sticks plot function for stock analysis.
                All four arguments, open, close, high and low, are mandatory.

                :param open: open price series
                :type open: pandas series
                :param close: close price series
                :type close: pandas series
                :param high: high price series
                :type high: pandas series
                :param low: low price series
                :type low: pandas series
        """
        if self.candle == True:
            print("Overwrite the previous candle plot.")
            print("Only one candle stick plot is allowed.")
        self.series["open"] = open
        self.series["high"] = high
        self.series["low"] = low
        self.series["close"] = close
        self.set_options(plotter="candlePlotter")
        self.set_options(customBars=False)
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option["series"]["open"][key] = value
                self.option["series"]["high"][key] = value
                self.option["series"]["low"][key] = value
                self.option["series"]["close"][key] = value
    def annotate(self, series, x, shortText, text=""):
        """ 
            To annotate a particular point in the plot.

            :param series: series name
            :param x: the x coordinate for the annotation.
            :param shortText: Short Text to display on the plot.
            :param text: the text shown when the mouse is on top of the short text.
        """
        a = {}
        a["series"] = series
        a["shortText"] = shortText
        a["x"] = x
        a["text"] = text
        self.annotations.append(a)
    def set_axis_options(self, axis, **kwargs):
        """ 
            To set the option of an axis.
            Please find the options on `dygraphs.com
            <http://dygraphs.com/options.html#Axis%20display>`_.

            :param axis: "x", "y" or "y2"
            :type axis: string

            For example, to set the label of x axis of g to red.
            ::
                g.set_axis_options(axis="x",axisLabelColor="red")
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option['axes'][axis][key] = value
    def set_series_options(self, series, **kwargs):
        """ 
            To set the option of a series.
            Please find the options on `dygraphs.com
            <http://dygraphs.com/options.html#Series>`_.

            :param series: series name
            :type series: string
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option['series'][series][key] = value
    def set_options(self, **kwargs):
        """ To set global option.
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option[key] = value
    def auto_range(self, axis="y"):
        """ To automatically adjust vertical range

                :param axis: "y" or "y2"
                :type axis: string
        """
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
    def savefig(self, csv_file="dyplot.csv", div_id="dyplot", js_vid="g", dt_fmt="%Y-%m-%d", \
        html_file=None, width="1024px", height="600px", csv_url=""):
        """ To save the plot to a html file or to return html code.

                :param csv_file: the csv file name
                :type csv_file: string
                :param csv_url: the csv url used by javascript
                :type csv_url: string
                :param div_id: div id to be used in html
                :type div_id: string
                :param js_vid: id to be used in javascript
                :type js_vid: string
                :param dt_fmt: date-time format if the seriers are time series.
                :type dt_fmt: string
                :param html_file: the file name of html file
                :type html_file: string
                :param width: The width of the plot
                :type width: int
                :param height: The height of the plot
                :type height: int
                :return div: the html code to be embedded in the webpage is return.
        """
        self.save_csv(csv_file, dt_fmt)
        if csv_url == "":
            csv_url = csv_file
        if self.option['axes']['y']['valueRange'] == []:
            self.auto_range(axis='y')
        if self.option['axes']['y2']['valueRange'] == []:
            self.auto_range(axis='y2')
        options = json.dumps(self.option)
        options = options.replace('"candlePlotter"', 'candlePlotter')
        div = '<div id="' + div_id + '" style="width:'+ width + '; height:' + height + ';"></div>\n'
        div += '<script type="text/javascript">\n'
        div += js_vid + ' = new Dygraph(\n'
        div += '    document.getElementById("' + div_id + '"),\n'
        div += '    "' + csv_url + '", // path to CSV file\n'
        div += options
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
        """ To save the plot to a html file.
        """
        header = """<html>
<head>
<script type="text/javascript" src="../js/dygraph-combined-dev.js"></script>
<script type="text/javascript" src="../js/dyplot.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)
    def save_csv(self, csv_file, dt_fmt):
        """ 
        To save all necessary data to a csv file.

            :param csv_file: csv file name
            :type csv_file: string
            :param dt_fmt: date time format if x-axis is date-time
            :type dt_fmt: string
        """
        csv_series = []
        if type(self.x[0]) == pandas.tslib.Timestamp:
            csv_series.append([])
            for e in self.x:
                csv_series[0].append(e.strftime(dt_fmt))
        else:
            csv_series.append(list(map(str, self.x)))
        names = []
        names.append(self.xname)
        if "plotter" in self.option and self.option["plotter"]== "candlePlotter":
            candle_list = ["open", "high", "low", "close"]
            names.extend(candle_list)
            for c in candle_list:
                csv_series.append(self.series[c].map(str))
                self.series = {key: value for key, value in self.series.items() if key != c}
        for s in self.series:
            if type(self.series[s]) == type({}):
                csv_series.append(self.series[s]['l'].map(str) + ";" + self.series[s]['m'].map(str) + ";" \
                    + self.series[s]['h'].map(str))
            else:
                if "plotter" in self.option and self.option["plotter"]== "candlePlotter":
                    csv_series.append(self.series[s].map(str))
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
