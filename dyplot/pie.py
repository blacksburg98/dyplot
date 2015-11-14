from dyplot.c3 import C3 as c3Core
class Pie(c3Core):
    def __init__(self, frac, labels):
        """
            To plot a pie chart.

            :param frac: The list to plot.
            :type frac: array_like. A list of float or int.
            :param labels: The list of the slice names.
            :type labels: array_like. A list of string.

            For example, the following would give a pie chart with three slices:
            30%, 20% and 50%.
            ::
                from dyplot.pie import Pie
                frac = [30, 20, 50]
                labels = ["setosa", "versicolor", "viginica"]
                g = Pie(frac=frac, labels=labels)
        """
        c3Core.__init__(self)
        self.option["data"]["type"] = "pie"
        for i in enumerate(frac):
            self.option["data"]["columns"].append([labels[i[0]], i[1]])
