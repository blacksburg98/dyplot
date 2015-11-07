from dyplot.c3.core import Core as c3Core
class Pie(c3Core):
    def __init__(self, frac, labels):
        c3Core.__init__(self)
        self.option["data"]["type"] = "pie"
        for i in enumerate(frac):
            self.option["data"]["columns"].append([labels[i[0]], i[1]])
