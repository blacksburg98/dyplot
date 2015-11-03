import datetime as dt
from finpy.financial.equity import get_tickdata
import finpy.utils.fpdateutil as du
from finpy.financial.portfolio import Portfolio
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
