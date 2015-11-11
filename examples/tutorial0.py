import datetime as dt
import numpy as np
import pandas as pd
from dyplot.dygraphs import Dygraphs
if __name__ == '__main__':
    foo = np.random.rand(100)
    boo = pd.Series(foo, index=range(0,100))
    dg = Dygraphs(boo.index, "date") 
    dg.plot(series="Random", mseries=boo)
    dg.set_options(title="Tutorial 0")
    div = dg.savefig(csv_file="tutorial0.csv", div_id="demodiv", js_vid="jid", html_file="tutorial0.html")
    print(div)
