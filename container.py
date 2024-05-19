from components import *

class Container:

    def __init__(self) -> None:
        self._accessibility = None
        self._annotations = None
        self._boost = None
        self._caption = None
        self._chart = None
        self._colors = None
        self._credits = None
        self._data = None
        self._defs = None
        self._drilldown = None
        self._exporting = None
        self._labels = None
        self._lang = None
        self._legend = None
        self._loading = None
        self._navigator = None
        self._pane = None
        self._plot_options = None
        self._range_selector = None
        self._responsive = None
        self._scrollbar = None
        self._series = None
        self._subtitle = None
        self._title = None
        self._tooltip = None
        self._x_axis = None
        self._y_axis = None        
        self._z_axis = None

    @property
    def accessibility(self):
        return self._accessibility
    
    @property
    def annotations(self):
        return self._annotations
    
    @property
    def boost(self):
        return self._boost
    
    @property
    def caption(self):
        return self._caption
    
    @property
    def chart(self):
        return self._chart
    
    @property
    def colors(self):
        return self._colors
    
    @property
    def credits(self):
        return self._credits
    
    @property
    def data(self):
        return self._data

    @property
    def defs(self):
        return self._defs
    
    @property
    def drilldown(self):
        return self._drilldown
    
    @property
    def exporting(self):
        return self._exporting
    
    @property
    def labels(self):
        return self._labels
    
    @property
    def lang(self):
        return self._lang
    
    @property
    def legend(self):
        return self._legend
    
    @property
    def loading(self):
        return self._loading
    
    @property
    def navigator(self):
        return self._navigator
    
    @property
    def pane(self):
        return self._pane
    
    @property
    def plot_options(self):
        return self._plot_options
    
    @property
    def range_selector(self):
        return self._range_selector
    
    @property
    def responsive(self):
        return self._responsive
    
    @property
    def scrollbar(self):
        return self._scrollbar
    
    @property
    def series(self):
        return self._series

    @property
    def subtitle(self):
        return self._subtitle

    @property
    def title(self):
        return self._title
    
    @property
    def tooltip(self):
        return self._tooltip
    
    @property
    def x_axis(self):
        return self._x_axis
    
    @property
    def y_axis(self):
        return self._y_axis
    
    @property
    def z_axis(self):
        return self._z_axis

    @accessibility.setter
    def accessibility(self,value):
        self.__setter_attributes(attr_name='accessibility', class_name="Accessibility", value=value)

    @accessibility.setter
    def annotations(self,value):
        self.__setter_attributes(attr_name='annotations', class_name="Annotations", value=value)
    
    @boost.setter
    def boost(self,value):
        self.__setter_attributes(attr_name='boost', class_name="Boost", value=value)
    
    @caption.setter
    def caption(self,value):
        self.__setter_attributes(attr_name='caption', class_name="Caption", value=value)
    
    @chart.setter
    def chart(self,value):
        self.__setter_attributes(attr_name='chart', class_name="Chart", value=value)

    @colors.setter
    def colors(self,value):
        self.__setter_attributes(attr_name='colors', class_name="Colors", value=value)
    
    @credits.setter
    def credits(self,value):
        self.__setter_attributes(attr_name='credits', class_name="Credits", value=value)
    
    @data.setter
    def data(self,value):
        self.__setter_attributes(attr_name='data', class_name="Data", value=value)
    
    @defs.setter
    def defs(self,value):
        self.__setter_attributes(attr_name='defs', class_name="Defs", value=value)
    
    @drilldown.setter
    def drilldown(self,value):
        self.__set_attributes(attr_name='drilldown', class_name="Drilldown", value=value)
    
    @exporting.setter
    def exporting(self,value):
        self.__setter_attributes(attr_name='exporting', class_name="Exporting", value=value)
    
    @labels.setter
    def labels(self,value):
        self.__setter_attributes(attr_name='labels', class_name="Labels", value=value)

    @lang.setter
    def lang(self,value):
        self.__setter_attributes(attr_name='lang', class_name="Lang", value=value)
    
    @legend.setter
    def legend(self,value):
        self.__setter_attributes(attr_name='legend', class_name="Legend", value=value)
    
    @loading.setter
    def loading(self,value):
        self.__setter_attributes(attr_name='loading', class_name="Loading", value=value)
    
    @navigator.setter
    def navigator(self,value):
        self.__setter_attributes(attr_name='navigator', class_name="Navigator", value=value)
    
    @pane.setter
    def pane(self,value):
        self.__setter_attributes(attr_name='pane', class_name="Pane", value=value)
    
    @plot_options.setter
    def plot_options(self,value):
        self.__setter_attributes(attr_name='plot_options', class_name="PlotOptions", value=value)
    
    @range_selector.setter
    def range_selector(self,value):
        self.__setter_attributes(attr_name='range_selector', class_name="RangeSelector", value=value)
    
    @responsive.setter
    def responsive(self,value):
        self.__set_attributes(attr_name='responsive', class_name="Responsive", value=value)
    
    @scrollbar.setter
    def scrollbar(self,value):
        self.__setter_attributes(attr_name='scrollbar', class_name="Scrollbar", value=value)
    
    @series.setter
    def series(self,value):
        self.__setter_attributes(attr_name='series', class_name="Series", value=value)

    @subtitle.setter
    def subtitle(self,value):
        self.__setter_attributes(attr_name='subtitle', class_name="Subtitle", value=value)

    @title.setter
    def title(self,value):
        self.__setter_attributes(attr_name='title', class_name="Title", value=value)
    
    @tooltip.setter
    def tooltip(self,value):
        self.__setter_attributes(attr_name='tooltip', class_name="Tooltip", value=value)
    
    @x_axis.setter
    def x_axis(self,value):
        self.__setter_attributes(attr_name='x_axis', class_name="XAxis", value=value)
    
    @y_axis.setter
    def y_axis(self,value):
        self.__setter_attributes(attr_name='y_axis', class_name="YAxis", value=value)
    
    @z_axis.setter
    def z_axis(self,value):
        self.__setter_attributes(attr_name='z_axis', class_name="ZAxis", value=value)

    def __setter_attributes(self, attr_name, class_name, value):
        """
        Dynamically sets attributes of the HighChart. The value can be an object, a dictionary with properties, or a list of objects/dictionaries.
        
        Parameters:
            attr_name (str): The name of the attribute to set ('title', 'subtitle', 'chart', 'legend', etc.).
            value (object | dict | list): The new object, a dictionary to create/update the attribute, or a list of objects/dictionaries.
            class_name (str): The name of the class to which the attribute should conform.
        """
        class_ = globals()[class_name]  # Assumes classes are in the same module or are imported

        if isinstance(value, list):
            setattr(self, f"_{attr_name}", class_.from_list(value))

        elif isinstance(value, dict):
            setattr(self, f"_{attr_name}", class_.from_dict(value))

        elif isinstance(value, class_):
            setattr(self, f"_{attr_name}", value)

        else:
            raise TypeError(f"{attr_name} must be a {class_name} object, a dictionary of properties, or a list of either.")