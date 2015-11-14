from dyplot.c3 import C3 as Core
import numpy as np
class Hist(Core):
    """
    Compute the histogram of a set of data.
    """
    def __init__(self, a, bins=10, r=None, weights=None, density=None, xlabel = "", **kwargs):
        """

            :param a: input data. The histogram is computed over the flattened array.
            :type a: array_like
            :param bins: The lower and upper range of the bins. 
                If not provided, range is simply (a.min(), a.max()). 
                Values outside the range are ignored.
            :type bins: (float, float), optional
            :param weights: An array of weights, of the same shape as a. 
                Each value in a only contributes its associated weight towards the bin count (instead of 1). 
                If normed is True, the weights are normalized, so that the integral of the density over the range remains 1
            :type weights: bool, optional
            :param density: If False, the result will contain the number of samples in each bin. 
                If True, the result is the value of the probability density function at the bin, normalized such that the integral over the range is 1. Note that the sum of the histogram values will not be equal to 1 unless bins of unity width are chosen; it is not a probability mass function. 
                Overrides the normed keyword if given.
            :type density: bool, optional
            :param xlabel: The name of the x label.
            :type xlabel: string
        """
        Core.__init__(self, option=kwargs)
        hist, bin_edges  = np.histogram(a, bins, r, weights, density)
        h = map(int, hist)
        self.option["data"]["type"] = "bar"
        columns = []
        columns.append(xlabel)
        columns.extend(h)
        self.option["data"]["columns"].append(columns)
        self.option["bar"] = {}
        self.option["bar"]["width"] = {}
        self.option["bar"]["width"]["ratio"] = 0.5
        labels = []
        for i in range(0, len(bin_edges)-1):
            labels.append(str(bin_edges[i]) + "-" + str(bin_edges[i+1]))
        self.set_xticklabels(labels, "categories")
