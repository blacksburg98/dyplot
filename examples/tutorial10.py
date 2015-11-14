import datetime as dt
import numpy as np
import pandas as pd
import csv
from dyplot.dygraphs import Dygraphs
if __name__ == '__main__':
    foo = map(float, np.random.rand(100))
    roo = map(lambda x: x*0.01, range(0, 100))
    print(roo)
    with open('t.csv', 'w') as csvfile:
        cw = csv.writer(csvfile)
        for i in zip(roo, foo):
            print(i)
            cw.writerow(i)
