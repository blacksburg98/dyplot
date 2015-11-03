import datetime as dt
from finpy.financial.equity import get_tickdata
import finpy.utils.fpdateutil as du
from finpy.financial.portfolio import Portfolio
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
