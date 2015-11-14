from dyplot.nvd3 import NVD3 
import csv
class Scatter(NVD3):
    def __init__(self, x, y, s=1, marker='o', c='b', g='g', option={}):
        """ 
        To plot a scatter chart.

            :param x, y: x, y coordinate
            :type x: array_like
            :param s: The sizes of each data point. 
            :type s: int or a list of int
            :param marker: 
            1. 'o' : circle
            2. '+' : cross 
            3. '^' : triangle-up 
            4. 'v' : triangle-down
            5. 'D' : diamond 
            6. 's' : square
            :type marker: string or a list of string
            :param g: The group name.
            :type g: string
        """
        self.option = {
            showDistX: true,
            showDistY: true,
            transitionDuration: 350,
            xtickformat: '.02f',
            ytickformat: '.02f',
            onlyCricles: false
        }
        for key in option:
            self.option[key] = option[key]
        self.data = {}
        self.__call__(x,y,s,marker,g)

    def __call__(self, x, y, s=1, marker='o', c='b'):
        length = len(x)
        if type(s) == type(1):
            sizes = s * length
        else:
            sizes = s
        if marker == type('o'):
            markers = marker * length
        else:
            markers = marker
        group = zip(x, y, s, markers)
        self.data[g] = group

    def savefig(self, csv_file="nvd3.csv", div_id="nvd3", html_file=None, width="400px", height="300px", csv_url=""):
        """ 
        To save the plot to a html file or to return html code.

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
            :param width: The width of the plot. For exampe, "400px".
            :type width: string
            :param height: The height of the plot. For example, "300px".
            :type height: string
            :return div: the html code to be embedded in the webpage is return.
        """
        self.save_csv(csv_file)
        div = '<style>\n#' + div_id + "svg { height:" + height + "; width: " + width + ";}\n"
        div += '</style>'
        div += '<div id="' + div_id + '"></div>\n'
        div += '<script>\n'
        div += 'scatter_chart({chart_data : "test.csv", div : "chart", options : {}})'
        div += '</script>\n'
        if type(html_file) != type(None):
            self._save_html(html_file, div)
        return div
    def _save_html(self, html_file, div):
        header = """<html>
<head>
<link href="../stylesheets/nv.d3.css" rel="stylesheet">
<script src="../js/jquery-1.11.3.min.js"></script>
<script src="../js/d3.v3.js"></script>
<script src="../js/nv.d3.js"></script>
<script src="../js/dyplot.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)

    def save_csv(csv_file):
        lines = []
        mlen = 0
        for g in self.data:
            l = len(self.data[g])
            if l > mlen:
                mlen = l
