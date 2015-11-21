import json
class NVD3():
    def __init__(self, option={}):
        """
        option needs to be a structure like the dictinary of options.
        """
    def dump_option(self):
        """
            :return option: return the instance variable option.
        """
        return self.option
    def set_options(self, **kwargs):
        """ To set global option.
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.option[key] = value
    def gen_options(self):
        """ To generate options of nvd3 charts.
        """
        o = ""
        for key in self.option:
            os = json.dumps(self.option[key])
            if key == "color":
                fs = os.replace('\"', '')
            else:
                fs = os
            o += '    .' + key + '(' + fs + ')\n'
        return o
    def set_axis_options(self, axis, **kwargs):
        """ To set axis options.
                :param axis: "xAsix" or "yAxis"
                :type axis: string
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.axis[axis][key] = value
    def gen_axis_options(self):
        """ To generate options of axis
        """
        o = ""
        for z in self.axis:
            for key in self.axis[z]:
                os = json.dumps(self.axis[z][key])
                if key == "tickFormat":
                    fs = os.replace('\"', '')
                o += "    chart." + z + "." + key + "(" + fs + ");\n"
        return o 

