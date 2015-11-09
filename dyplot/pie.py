from dyplot.core import Core as c3Core
class Pie(c3Core):
    def __init__(self, frac, labels):
        """
        To plot a pie chart.

            :param frac: the list to plot.
            :param labels: A axis label.

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
