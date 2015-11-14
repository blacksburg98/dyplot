dyplot
======
matplotlib-like plot functions for dygraphs.js c3.js. 
See `dygraphs.com <http://dygraphs.com>`_ and 
`c3js.org <http://c3js.org>`_.
Interactive out of the box: zoom, pan and mouseover are on by default.
Drag your mouse to zoom in and double click to zoom out.
You can clone the source code from 
https://github.com/blacksburg98/dyplot
The series needs to be pandas.Series

Tutorial 2. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial2.html 
::

    import datetime as dt
    from finpy.equity import get_tickdata
    import finpy.fpdateutil as du
    from finpy.portfolio import Portfolio
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        ls_symbols = ['AAPL','XOM', 'MSFT', 'WMT']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_data = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        all_stocks = Portfolio(all_data, 0, ldt_timestamps, [])
        dg = Dygraphs(ldt_timestamps, "date") 
        for tick in ls_symbols:
            dg.plot(series=tick, mseries=all_stocks.normalized(tick))
        dg.set_options(title="Tutorial 2")
        div = dg.savefig(csv_file="tutorial2.csv", html_file="tutorial2.html")

Tutorial 3. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial3.html 
::

    import datetime as dt
    from finpy.equity import get_tickdata
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
    from finpy.equity import get_tickdata
    import finpy.fpdateutil as du
    from finpy.portfolio import Portfolio
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        ls_symbols = ['AAPL','$RUA']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_data = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        all_stocks = Portfolio(all_data, 0, ldt_timestamps, [])
        dg = Dygraphs(ldt_timestamps, "date") 
        dg.plot(series="AAPL", mseries=all_data["AAPL"]['close'], axis='y2')
        dg.plot(series="Russel 3000", mseries=all_data["$RUA"]['close'])
        max_ratio = max(all_stocks.normalized("AAPL").max(), all_stocks.normalized("$RUA").max())
        min_ratio = min(all_stocks.normalized("AAPL").min(), all_stocks.normalized("$RUA").min())
        max_ratio *= 1.05
        min_ratio *= 0.95
        dg.set_axis_options(axis='y', valueRange=[all_data["$RUA"]['close'][0]*min_ratio, \
            all_data["$RUA"]['close'][0]*max_ratio])
        dg.set_axis_options(axis='y2', valueRange=[all_data["AAPL"]['close'][0]*min_ratio, \
            all_data["AAPL"]['close'][0]*max_ratio])
        dg.annotate('AAPL', '2010-06-21', "B", "Buy on 2010-06-21")
        dg.annotate('AAPL', '2010-08-13', "S", "Sell on 2010-08-13")
        dg.set_options(title="Tutorial 4", ylabel="Russel 3000", y2label="AAPL")
        div = dg.savefig(csv_file="tutorial4.csv", html_file="tutorial4.html")

Tutorial 7. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial7.html 
::

    import datetime as dt
    from finpy.equity import get_tickdata
    import finpy.fpdateutil as du
    from finpy.portfolio import Portfolio
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2014, 1, 1)
        dt_end = dt.datetime(2014, 12, 31)
        ls_symbols = ['AAPL']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
        p = Portfolio(all_stocks, 0, ldt_timestamps) 
        p.normalized_price(tick="AAPL")
        dg = Dygraphs(ldt_timestamps, "date") 
        dg.candleplot(open=p.equities["AAPL"]['open'],
                      high=p.equities["AAPL"]['high'],
                      low=p.equities["AAPL"]['low'],
                      close=p.equities["AAPL"]['close'])
        dg.set_options(title="Tutorial 7")
        div = dg.savefig(csv_file="tutorial7.csv", html_file="tutorial7.html")
Tutorial 8. 
===========
See the output at http://store-demo.appspot.com/tutorial/tutorial8.html 
::

    import datetime as dt
    from finpy.equity import get_tickdata
    import finpy.fpdateutil as du
    from finpy.portfolio import Portfolio
    from dyplot.dygraphs import Dygraphs
    if __name__ == '__main__':
        dt_timeofday = dt.timedelta(hours=16)
        dt_start = dt.datetime(2014, 9, 1)
        dt_end = dt.datetime(2014, 12, 31)
        ls_symbols = ['AAPL']
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
        all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps, source="Google")
        p = Portfolio(all_stocks, 0, ldt_timestamps) 
        dg = Dygraphs(ldt_timestamps, "date") 
        dg.candleplot(open=p.equities["AAPL"]['open'],
                      high=p.equities["AAPL"]['high'],
                      low=p.equities["AAPL"]['low'],
                      close=p.equities["AAPL"]['close'])
        dg.plot(series="10D MA", mseries=p.moving_average(window=20, tick="AAPL"))
        dg.set_options(title="Tutorial 8")
        div = dg.savefig(csv_file="tutorial8.csv", html_file="tutorial8.html")
