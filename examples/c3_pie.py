from dyplot.pie import Pie
frac = [30, 20, 50]
labels = ["setosa", "versicolor", "viginica"]
g = Pie(frac=frac, labels=labels)
c = {}
c["columns"] = []
c["columns"].append(["setosa", 100])
g.animate("load", c, 1000)
g.savefig(html_file="c3_pie.html")
