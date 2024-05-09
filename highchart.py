# highchart.py
from components import *
from templates import DEFAULT_TEMPLATE
from container import Container

class Highchart(Container):
    """ 
    """
    def __init__(self):
        super().__init__()
        self.__init_default_template()
        
    def __init_default_template(self):
        pass    

    def __set_attributes(self, component_attr, component_class, *args, **kwargs):
        """
        Generic method to set or update components of the Highchart.

        Args:
            component_attr (str): The attribute name of the component (e.g., "_chart", "_title").
            component_class (type): The class of the component to be instantiated (e.g., Chart, Title).
            *args: Positional arguments required by the component.
            **kwargs: Keyword arguments for the component properties.
        """
        component = getattr(self, component_attr, None)
        if component is None:
            # If the component doesn"t exist, create a new instance
            setattr(self, component_attr, component_class(*args, **kwargs))
        else:
            # If the component exists, update its properties
            for key, value in kwargs.items():
                setattr(component, key, value)

    def set_legend(self,enable:bool=True,**kwargs):
        kwargs.update({"enable": enable})
        self.__set_attributes("_legend", Legend, **kwargs)

    def set_chart(self,type:str=None,**kwargs):
        kwargs.update({"type": type})
        self.__set_attributes("_chart", Chart, type, **kwargs)

    def set_title(self, text:str=None, align:str=None,**kwargs):
        kwargs.update({"text": text, "align": align})
        self.__set_attributes("_title", Title, text, align, **kwargs)

    def set_subtitle(self,text:str=None, align:str=None,**kwargs):
        kwargs.update({"text": text, "align": align})
        self.__set_attributes("_subtitle", Subtitle, text, align, **kwargs)

    def set_x_axis(self,**kwargs):
        self.__set_attributes("_x_axis", XAxis, **kwargs)

    def set_y_axis(self,**kwargs):
        self.__set_attributes("_y_axis", YAxis, **kwargs)

    def set_tooltip(self,**kwargs):
        self.__set_attributes("_tooltip", Tooltip, **kwargs)

    def set_accessibility(self,description:str,**kwargs):
        self.__set_attributes("_accessibility", Accessibility, description, **kwargs)

    def set_colors(self,colors:list,**kwargs):
        self.__set_attributes("_colors", Colors, colors, **kwargs)

    def add_series(self, series):
        """
        Adds a new series to the chart.

        Args:
            series (Series): A Series object to add to the chart.
        """
        
        if not isinstance(series, Series):
            raise ValueError("Must provide a Series object.")
        
        if not self._series:
            self._series = []

        self._series.append(series)

    def add_series_from_dataframe(self, dataframe, column_name, series_name, drilldown, **kwargs):
        """
        Directly creates and adds a series from a pandas DataFrame to the chart.

        Args:
            dataframe (pd.DataFrame): The DataFrame containing the series data.
            column_name (str): The column in the DataFrame to use as data for the series.
            series_name (str): The name of the series.
            **kwargs: Additional keyword arguments for the series (e.g., type, color).
        """
        if column_name not in dataframe.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
        
        data = dataframe[column_name].tolist()
        series = Series(name=series_name, data=data, **kwargs)
        self.add_series(series)

    def add_y_axis(self, y_axis):

        if not isinstance(y_axis, YAxis):
            raise ValueError("Must provide a YAxis object.")
        

    def get_template(self, name: str = None) -> dict:
        """
        Retrieves a chart configuration template by its name from a predefined dictionary of templates.

        Args:
            name (str): The name of the template to retrieve.

        Returns:
            dict: The template dictionary if found.

        Raises:
            ValueError: If the template name is not provided or the template does not exist.
        """
        if not name:
            raise ValueError("Template name is missing. Please specify a valid template name.")
        
        try:
            return TEMPLATES[name]
        except KeyError:
            raise ValueError(f"Template named '{name}' does not exist in the predefined templates.")

    def get_list_template(self) -> list:
        """
        Retrieves a list of all available template names from the predefined TEMPLATES dictionary.

        Returns:
            list: A list of template names.
        """
        return list(TEMPLATES.keys())
    
    def load_template(self, template:dict=None):
        """
        Applies a template to the chart. The template should be a dictionary with possible keys
        for "title", "subtitle", and "series", each containing further settings.

        Args:
            template (dict): A dictionary containing the chart configuration.
        """

        if template is None:
            raise ValueError("Template must be provided and cannot be None")

        if "chart" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.chart = Chart.from_dict(template["chart"])

        if "title" in template:
            # Assumes Title has a from_dict class method or similar functionality
            self.title = Title.from_dict(template["title"])
        
        if "subtitle" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.subtitle = Subtitle.from_dict(template["subtitle"])

        if "legend" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.legend = Legend.from_dict(template["legend"])

        if "xAxis" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._x_axis = XAxis.from_dict(template["xAxis"])

        if "yAxis" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._y_axis = YAxis.from_dict(template["yAxis"])

        if "plotOptions" in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._plot_options = PlotOptions.from_dict(template["plotOptions"])

        if "series" in template:
            # Clear existing series and add new ones from the template
            # self.series.clear()
            # for serie_data in template["series"]:
            #     # Assumes Series has a from_dict class method or similar functionality
            #     self.series.append(Series.from_dict(serie_data))
            pass

    def render(self):
        """
        Generates a dictionary representation of the chart object, including only available components.

        Returns:
            dict: A dictionary with keys for "chart", "title", "subtitle", and "series" if they exist.
        """
        result = {}
        if self._chart:
            result["chart"] = self._chart.to_dict()
        if self._title:
            result["title"] = self._title.to_dict()
        if self._subtitle:
            result["subtitle"] = self._subtitle.to_dict()
        if self._legend:
            result["legend"] = self._legend.to_dict()
        if self._series:
            result["series"] = [serie.to_dict() for serie in self._series]
        
        return result