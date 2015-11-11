from dyplot.hist import Hist
a = [3,4,4,5,6,6,6,6,5,9,3,3,4,4,5,6,7,8,9,3,2,2,4,5]
g = Hist(a, xlabel="Frequency")
g.savefig(html_file="tutorial9.html")
