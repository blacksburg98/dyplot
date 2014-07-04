from dyplot.c3.general import General as c3General
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
g = c3General(option)
c = []
c.append(["setosa", 100])
g.animate("load", c, 1000)
g.savefig(html_file="general.html")
