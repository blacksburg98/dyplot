from dyplot.core import Core 
class Bar(Core):
    def __init__(self, height, label):
        """ 
            To plot a bar chart.

            :param height: The data to plot. A list of data.
            :type height: array_like
            :param label: The name of the data.
            :type label: string 
        """
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

