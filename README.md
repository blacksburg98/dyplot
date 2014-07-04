dyplot
======
matplotlib-like plot functions for dygraphs.js. See dygraphs.com for detail.
Interactive out of the box: zoom, pan and mouseover are on by default.
Drag your mouse to zoom in and double click to zoom out.
You can clone the source code from 
https://github.com/blacksburg98/dyplot
The series needs to be pandas.Series
Tutorial 1. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial1.html 
::

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
    div = dg.savefig(csv_file="tutorial.csv", html_file="tutorial1.html")

Tutorial 2. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial2.html 
::

    import datetime as dt
    from finpy.utils import get_tickdata
    import finpy.fpdateutil as du
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        ls_symbols = ['AAPL','XOM', 'MSFT', 'WMT']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        dg = Dygraphs(ldt_timestamps, "date") 
        for tick in ls_symbols:
            dg.plot(series=tick, mseries=all_stocks[tick].normalized())
        dg.set_options(title="Tutorial 2")
        div = dg.savefig(csv_file="tutorial2.csv", html_file="tutorial2.html")
Tutorial 3. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial3.html 
::

    import datetime as dt
    from finpy.utils import get_tickdata
    import finpy.fpdateutil as du
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        ls_symbols = ['AAPL','$RUA']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        dg = Dygraphs(ldt_timestamps, "date") 
        dg.plot(series="AAPL", mseries=all_stocks["AAPL"]['close'], axis='y2')
        dg.plot(series="$RUA", mseries=all_stocks["$RUA"]['close'])
        dg.set_options(title="Tutorial 3")
        div = dg.savefig(csv_file="tutorial3.csv", html_file="tutorial3.html")
Tutorial 4. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial4.html 
:: 

    import datetime as dt
    from finpy.utils import get_tickdata
    import finpy.fpdateutil as du
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        ls_symbols = ['AAPL','$RUA']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        dg = Dygraphs(ldt_timestamps, "date") 
        dg.plot(series="AAPL", mseries=all_stocks["AAPL"]['close'], axis='y2')
        dg.plot(series="$RUA", mseries=all_stocks["$RUA"]['close'])
        max_ratio = max(all_stocks["AAPL"].normalized().max(), all_stocks["$RUA"].normalized().max())
        min_ratio = min(all_stocks["AAPL"].normalized().min(), all_stocks["$RUA"].normalized().min())
        max_ratio *= 1.05
        min_ratio *= 0.95
        dg.set_axis_options(axis='y', valueRange=[all_stocks["$RUA"]['close'][0]*min_ratio, \
            all_stocks["$RUA"]['close'][0]*max_ratio])
        dg.set_axis_options(axis='y2', valueRange=[all_stocks["AAPL"]['close'][0]*min_ratio, \
            all_stocks["AAPL"]['close'][0]*max_ratio])
        dg.set_options(title="Tutorial 4")
        div = dg.savefig(csv_file="tutorial4.csv", html_file="tutorail4.html")
