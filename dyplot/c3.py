import json
class C3():
    def __init__(self, option={}):
        """
        options needs to be a structure like the argument of c3.generate.
        """
        self.option = option
        self.option["axis"] = {}
        self.option["axis"]["x"] = {}
        self.option["axis"]["y"] = {}
        self.option["data"] = {}
        self.option["data"]["columns"] = []
        self.animation = []
    def dump_option(self):
        """
            :return option: return the instance variable option.
        """
        return self.option
    def animate(self, action, arguments, time):
        """
        To use animation on the chart.
        """
        a = {}
        a["action"] = action
        a["arguments"] = arguments
        a["time"] = time
        self.animation.append(a)
    def savefig(self, div_id="c3general", js_vid="g", html_file=None, width="400px", height="300px"):
        """
            To generate the html code to be embedded in html.

            :param div_id: The div id for html code
            :type div_id: string
            :param js_vid: The javascript c3 object.
            :type js_vid: string
            :param html_file: Save the html code to a html file if specified. "400px" or "50%".
            :type html_file: string
            :param width: The width of the chart. The format is the same as html width. 
            :type width: string
            :param height: The height of the chart. The format is the same as html height. 
            :type height: string
        """
        self.option["bindto"] = '#' + div_id 
        self.option["onmouseover"] = 'function (d, i) { console.log(\'onmouseover\', d, i, this); }'
        self.option["onmouseout"] = 'function (d, i) { console.log(\'onmouseout\', d, i, this); }'
        self.option["onclick"] = 'function (d, i) { console.log(\'onclick\', d, i, this); }'
        div = '<div id="' + div_id + '" style="width:'+ width + '; height:' + height + ';"></div>\n'
        div += '<script>\n'
        div += js_vid + ' = c3.generate(\n'
        div += json.dumps(self.option)
        div += '  );\n'
        for a in self.animation:
            div += "setTimeout(function () {" + js_vid + "." + a["action"] + "("
            div += json.dumps(a["arguments"]) + ');\n'
            div += '},' + str(a["time"]) + ');\n' 
        div += '</script>\n'
        if type(html_file) != type(None):
            self._save_html(html_file, div)
        return div
    def _save_html(self, html_file, div):
        header = """<html>
<head>
<link rel="stylesheet" type="text/css" href="../stylesheets/c3.min.css">
<script type="text/javascript" src="../js/d3.min.js"></script>
<script type="text/javascript" src="../js/c3.min.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)
    def set_xticklabels(self, labels, t=""):
        """
            To set the labels of x axis.

            :param labels: A list of t. 
            :type labels: array_like 
            :param t: "timeseries", "categories" or "indexed"
        """
        self.option["axis"]["x"]["type"] = t
        if t == "categories":
            self.option["axis"]["x"]["categories"] = labels
