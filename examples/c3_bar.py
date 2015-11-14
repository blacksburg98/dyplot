from dyplot.bar import Bar
h = [30, 20, 50, 40]
label = "setosa"
g = Bar(height=h, label=label)
h2 = [50, 30, 20, 30]
label2 = "barora"
h3 = [40, 20, 10, 50]
label3 = "exama"
g = Bar(height=h, label=label)
g(height=h2, label=label2)
g(height=h3, label=label3)
g.set_xticklabels(["G1", "G2", "G3", "G4"], "category")
g.savefig(html_file="c3_bar.html")
