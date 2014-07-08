from dyplot.c3.core import Core as c3Core
columns = []
columns.append(["setosa", 30])
columns.append(["versicolor", 20])
columns.append(["vigginica", 50])
data = {}
data["columns"] = columns
data["type"] = "pie"
axis = {}
axis["x"] = {}
axis["y"] = {}
axis["x"]["label"] = 'Sepal.Width'
axis["y"]["label"] = 'Pepal.Width'
option = {}
option["data"] = data
option["axis"] = axis
g = c3Core(option)
c = {}
c["columns"] = []
c["columns"].append(["setosa", 100])
g.animate("load", c, 1000)
g.savefig(html_file="tutorial5.html")
