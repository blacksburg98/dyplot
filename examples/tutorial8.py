
import datetime as dt
from finpy.financial.equity import get_tickdata
import finpy.utils.fpdateutil as du
from finpy.financial.portfolio import Portfolio
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
