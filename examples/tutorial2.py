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
