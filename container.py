from components import *

class Container:

    def __init__(self) -> None:
        self._accessibility = None
        self._boost = None
        self._chart = None
        self._colors = None
        self._credits = None
        self._defs = None
        self._drilldown = None
        self._exporting = None
        self._labels = None
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
    def boost(self):
        return self._boost
    
    @property
    def chart(self):
        return self._chart
    
    @property
    def credits(self):
        return self._credits
    
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

    def __set_attributes(self, attr_name, value):
        """
        Dynamically sets attributes of the HighChart. The value can be an object or a dictionary with properties.

        Parameters:
            attr_name (str): The name of the attribute to set ('title', 'subtitle', 'chart', 'legend').
            value (object | dict): The new object or a dictionary to create/update the attribute.
            class_dict (dict): A dictionary mapping attribute names to their respective classes.
        """
        class_name = attr_name.capitalize()  # Assumes class names are capitalized attribute names
        class_ = globals()[class_name]  # Assumes classes are in the same module or are imported

        if isinstance(value, class_):
            setattr(self, f"_{attr_name}", value)
        elif isinstance(value, dict):
            # Update or create a new object from dictionary using a from_dict class method
            setattr(self, f"_{attr_name}", class_.from_dict(value))
        else:
            raise TypeError(f"{class_name} must be a {class_name} object or a dictionary of properties.")

    @accessibility.setter
    def accessibility(self,value):
        self.__set_attributes(attr_name='accessibility', value=value)
    
    @boost.setter
    def boost(self,value):
        self.__set_attributes(attr_name='boost', value=value)
    
    @chart.setter
    def chart(self,value):
        self.__set_attributes(attr_name='chart', value=value)
    
    @credits.setter
    def credits(self,value):
        self.__set_attributes(attr_name='credits', value=value)
    
    @defs.setter
    def defs(self,value):
        self.__set_attributes(attr_name='defs', value=value)
    
    @drilldown.setter
    def drilldown(self,value):
        self.__set_attributes(attr_name='drilldown', value=value)
    
    @exporting.setter
    def exporting(self,value):
        self.__set_attributes(attr_name='exporting', value=value)
    
    @labels.setter
    def labels(self,value):
        self.__set_attributes(attr_name='labels', value=value)
    
    @legend.setter
    def legend(self,value):
        self.__set_attributes(attr_name='legend', value=value)
    
    @loading.setter
    def loading(self,value):
        self.__set_attributes(attr_name='loading', value=value)
    
    @navigator.setter
    def navigator(self,value):
        self.__set_attributes(attr_name='navigator', value=value)
    
    @pane.setter
    def pane(self,value):
        self.__set_attributes(attr_name='pane', value=value)
    
    @plot_options.setter
    def plot_options(self,value):
        self.__set_attributes(attr_name='plot_options', value=value)
    
    @range_selector.setter
    def range_selector(self,value):
        self.__set_attributes(attr_name='range_selector', value=value)
    
    @responsive.setter
    def responsive(self,value):
        self.__set_attributes(attr_name='responsive', value=value)
    
    @scrollbar.setter
    def scrollbar(self,value):
        self.__set_attributes(attr_name='scrollbar', value=value)
    
    @series.setter
    def series(self,value):
        self.__set_attributes(attr_name='series', value=value)

    @subtitle.setter
    def subtitle(self,value):
        self.__set_attributes(attr_name='subtitle', value=value)

    @title.setter
    def title(self,value):
        self.__set_attributes(attr_name='title', value=value)
    
    @tooltip.setter
    def tooltip(self,value):
        self.__set_attributes(attr_name='tooltip', value=value)
    
    @x_axis.setter
    def x_axis(self,value):
        self.__set_attributes(attr_name='x_axis', value=value)
    
    @y_axis.setter
    def y_axis(self,value):
        self.__set_attributes(attr_name='y_axis', value=value)
    
    @z_axis.setter
    def z_axis(self,value):
        self.__set_attributes(attr_name='z_axis', value=value)