from dyplot.nvd3 import NVD3 
import csv
import json
class Scatter(NVD3):
    m2s = {'o' : 'circle',
         '+' : 'cross' ,
         '^' : 'triangle-up' ,
         'v' : 'triangle-down',
         'D' : 'diamond' ,
         's' : 'square'}
    def __init__(self, x, y, g,s=1, marker='o', slope="", intercept="", option={}):
        """ To plot a scatter chart.
            If slope and intercept are defined, then a line will be drawn.

                :param x, y: x, y coordinate
                :type x, y: array_like.
                :param s: The sizes of each data point. 
                :type s: int or a list of int
                :param marker: 
                    * 'o' : circle
                    * '+' : cross 
                    * '^' : triangle-up 
                    * 'v' : triangle-down
                    * 'D' : diamond 
                    * 's' : square
                :type marker: string or a list of string
                :param g: The group name.
                :type g: string
                :param slope: The slope of the line.
                :type slope: float
                :param intercept: The Y intercept of the line
                :type intercept: float
        """
        self.option = {
            "showDistX": True,
            "showDistY": True,
            "transitionDuration": 350,
            "xtickformat": '.02f',
            "ytickformat": '.02f',
            "onlyCricles": False
        }
        for key in option:
            self.option[key] = option[key]
        self.data = {}
        self.group = {}
        self.__call__(x,y,g,s,marker,slope,intercept)

    def __call__(self, x, y, g, s=1, marker='o', slope="", intercept=""):
        length = len(x)
        if isinstance(s, int):
            sizes = [s] * length
        else:
            sizes = s
        if isinstance(marker, str):
            markers = [Scatter.m2s[marker]] * length
        else:
            markers = map(lambda x: Scatter.m2s[x], marker)
        group = list(zip(x, y, sizes, markers))
        self.group[g] = {"slope": str(slope), "intercept": str(intercept)}
        self.data[g] = group

    def savefig(self, csv_file="nvd3.csv", div_id="nvd3", html_file=None, width="600px", height="400px", csv_url=""):
        """ To save the plot to a html file or to return html code.

                :param csv_file: the csv file name
                :type csv_file: string
                :param csv_url: the csv url used by javascript
                :type csv_url: string
                :param div_id: div id to be used in html
                :type div_id: string
                :param js_vid: id to be used in javascript
                :type js_vid: string
                :param html_file: the file name of html file
                :type html_file: string
                :param width: The width of the plot. For exampe, "400px".
                :type width: string
                :param height: The height of the plot. For example, "300px".
                :type height: string
                :return div: the html code to be embedded in the webpage is return.
        """
        self.save_csv(csv_file)
        if csv_url != "":
            csv_file = csv_url
        options = json.dumps(self.option)
        div = '<style>\n#' + div_id + " svg { height:" + height + "; width: " + width + ";}\n"
        div += '</style>'
        div += '<div id="' + div_id + '"><svg></svg></div>\n'
        div += '<script>\n'
        div += 'scatter_chart({chart_data:"' + csv_file + '", div :"' + div_id + '", options:'
        div += options + '})'
        div += '</script>\n'
        if type(html_file) != type(None):
            self._save_html(html_file, div)
        return div
    def _save_html(self, html_file, div):
        header = """<html>
<head>
<link href="../stylesheets/nv.d3.css" rel="stylesheet">
<script src="../js/jquery-1.11.3.min.js"></script>
<script src="../js/d3.min.js"></script>
<script src="../js/nv.d3.min.js"></script>
<script src="../js/dyplot.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)

    def save_csv(self, csv_file):
        lines = []
        mlen = 0
        head = []
        for g in self.data:
            g_head = ';'.join([g, self.group[g]["slope"], self.group[g]["intercept"]])
            head.append(g_head)
            l = len(self.data[g])
            if l > mlen:
                mlen = l
        lines.append(head)
        for i in range(0, mlen):
            line = []
            for g in self.data:
                try:
                    g_string = ';'.join(map(str, self.data[g][i]))
                    line.append(g_string)
                except:
                    line.append("")
            lines.append(line)
        with open(csv_file, 'w') as fp:
            cw = csv.writer(fp, lineterminator='\n', delimiter=',', quoting = csv.QUOTE_NONE)
            for ln in lines:
                cw.writerow(ln)
        
        
