import json
class Core():
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
        return self.option
    def animate(self, action, arguments, time):
        a = {}
        a["action"] = action
        a["arguments"] = arguments
        a["time"] = time
        self.animation.append(a)
    def savefig(self, div_id="c3general", js_vid="g", html_file=None, width="400px", height="300px"):
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
            self.save_html(html_file, div)
        return div
    def save_html(self, html_file, div):
        header = """<html>
<head>
<link rel="stylesheet" type="text/css" href="/stylesheets/c3.css">
<script type="text/javascript" src="/js/d3.min.js"></script>
<script type="text/javascript" src="/js/c3.min.js"></script>
</head><body>
"""
        footer = "</body></html>"
        with open(html_file, 'w') as f:
            f.write(header)
            f.write(div)
            f.write(footer)
    def set_xticklabels(self, labels, t=""):
        self.option["axis"]["x"]["type"] = t
        self.option["axis"]["x"]["categories"] = labels
