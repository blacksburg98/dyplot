import datetime as dt
from finpy.utils import get_tickdata
import finpy.fpdateutil as du
from dyplot.dyplot import Dyplot
if __name__ == '__main__':
    dt_timeofday = dt.timedelta(hours=16)
    dt_start = dt.datetime(2010, 1, 1)
    dt_end = dt.datetime(2010, 12, 31)
    ls_symbols = ['AAPL','$RUA']
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    all_stocks = get_tickdata(ls_symbols=ls_symbols, ldt_timestamps=ldt_timestamps)
    dg = Dyplot(ldt_timestamps, "date") 
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
    div = dg.savefig(csv_file="tutorial4.csv")
