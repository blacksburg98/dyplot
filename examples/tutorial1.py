import pandas as pd
from dyplot.dygraphs import Dygraphs
a = pd.Series([1,2,3,4,5,6,7,9,10])
b = pd.Series([1,3,5,9,2,8,5,5,15])
lc= pd.Series([1,3,4,5,6,7,9,3,2])
c = pd.Series([2,4,5,7,8,8,9,4,3])
hc= pd.Series([3,5,7,7,9,11,9,5,8])
dg = Dygraphs(a.index, "index")
dg.plot(series="a", mseries=a)
dg.plot(series="b", mseries=b)
dg.plot(series="c", mseries=c,lseries=lc, hseries=hc)
dg.set_options(title="Test")
dg.set_axis_options(axis="x",axisLabelColor="red")
div = dg.savefig(csv_file="tutorial1.csv", html_file="tutorial1.html")

