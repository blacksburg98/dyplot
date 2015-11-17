import numpy as np
import csv
from dyplot.scatter import Scatter
if __name__ == '__main__':
    x = np.random.rand(20)
    y = np.random.rand(20)
    s = Scatter(x, y, "Group 1")
    x = np.random.rand(10)
    y = np.random.rand(10)
    s(x, y, "Group 2", marker="+", s=[1,3,2,4,5,6,6,5,4,3])
    x = np.random.rand(10)
    y = np.random.rand(10)
    s(x, y, "Group 3", s=2, marker=["^", 'v', 'o', '+', 's', 's', 's', 'D', 'D', 'v'])
    s.savefig(csv_file="nvd3_scatter.csv",html_file="nvd3_scatter.html")
