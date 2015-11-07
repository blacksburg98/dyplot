from dyplot.c3.core import Core 
class Bar(Core):
    def __init__(self, height, label):
        Core.__init__(self)
        self.option["data"]["type"] = "bar"
        columns = []
        columns.append(label)
        columns.extend(height)
        self.option["data"]["columns"].append(columns)
        self.option["bar"] = {}
        self.option["bar"]["width"] = {}
        self.option["bar"]["width"]["ratio"] = 0.5
    def __call__(self, height, label):
        columns = []
        columns.append(label)
        columns.extend(height)
        self.option["data"]["columns"].append(columns)

