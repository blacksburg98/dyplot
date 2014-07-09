from dyplot.c3.core import Core as c3Core
class Pie(c3Core):
    def __init__(self, frac, labels):
        c3Core.__init__(self)
        data = {}
        data["type"] = "pie"
        columns = []
        for i in enumerate(frac):
            columns.append([labels[i[0]], i[1]])
        data["columns"] = columns
        self.option["data"] = data
