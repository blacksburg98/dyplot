dyplot
======
matplotlib-like plot functions for dygraphs.js. See dygraphs.com for detail.
If no html_file is provided, then no html file will be generated.
You can go to http://store-demo.appspot.com/temp.html to see the output of 
the short example.
https://github.com/blacksburg98/dyplot
The series needs to be pandas.Series
Short Example
=====
    import pandas as pd
    from dyplot import Dyplot
    a = pd.Series([1,2,3,4,5,6,7,9,10])
    b = pd.Series([1,3,5,9,2,8,5,5,15])
    lc= pd.Series([1,3,4,5,6,7,9,3,2])
    c = pd.Series([2,4,5,7,8,8,9,4,3])
    hc= pd.Series([3,5,7,7,9,11,9,5,8])
    dg = Dyplot(a.index, "index")
    dg.plot(name="a", mseries=a)
    dg.plot(name="b", mseries=b)
    dg.plot(name="c", mseries=c,lseries=lc, hseries=hc)
    div = dg.savefig(title="Test", html_file="temp.html")

