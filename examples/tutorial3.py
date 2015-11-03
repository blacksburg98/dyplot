
import datetime as dt
from finpy.financial.equity import get_tickdata
import finpy.utils.fpdateutil as du
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
