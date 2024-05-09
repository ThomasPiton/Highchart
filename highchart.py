
# highchart.py
from title import Title
from subtitle import Subtitle
from series import Series
from chart import Chart
from legend import Legend
from containers.drilldown import Drilldown
from plot_options import PlotOptions
from templates import TEMPLATES
from xaxis import XAxis
from yaxis import YAxis

class Highchart:
    def __init__(self):
        self._title = None
        self._legend = None
        self._chart = None
        self._subtitle = None
        self._series = None
        self._legend = None
        self._drilldown = None
        self._plot_options = None
        self._x_axis = None
        self._y_axis = None
        
        # self._z_axis = None
        # self._tooltip = None
        # self._credits = None
        # self._labels = None
        # self._navigation = None
        # self._responsive = None
        # self._annotations = None
        # self._no_data = None
        # self._color_axis = None
        # self._scrollbar = None
        # self._range_selector = None
        # self._boost = None
        # self._navigator = None

    @property
    def chart(self):
        """
        Provides access to the title object of the chart.

        Returns:
            Title: The current title object.
        """
        return self._chart
    
    @property
    def legend(self):
        """
        Provides access to the title object of the chart.

        Returns:
            Title: The current title object.
        """
        return self._legend

    @property
    def title(self):
        """
        Provides access to the title object of the chart.

        Returns:
            Title: The current title object.
        """
        return self._title

    @property
    def subtitle(self):
        """
        Provides access to the subtitle object of the chart.

        Returns:
            Title: The current subtitle object.
        """
        return self._subtitle

    @property
    def series(self):
        return self._series

    @title.setter
    def title(self, value):
        """
        Sets the title of the chart. The value can be a Title object or a dictionary with title properties.

        Parameters:
            value (Title | dict): The new title object or a dictionary to create/update the title.
        """
        if isinstance(value, Title):
            self._title = value
        elif isinstance(value, dict):
            # Update or create a new Title object from dictionary
            self._title = Title.from_dict(value)
        else:
            raise TypeError("Title must be a Title object or a dictionary of title properties.")
        
    @subtitle.setter
    def subtitle(self, value):
        """
        Sets the subtitle of the chart. The value can be a Subtitle object or a dictionary with subtitle properties.

        Parameters:
            value (Subtitle | dict): The new subtitle object or a dictionary to create/update the subtitle.
        """
        if isinstance(value, Subtitle):
            self._subtitle = value
        elif isinstance(value, dict):
            # Update or create a new Title object from dictionary
            self._subtitle = Subtitle.from_dict(value)
        else:
            raise TypeError("Title must be a Title object or a dictionary of title properties.")

    @chart.setter
    def chart(self, value):
        """
        Sets the chart. The value can be a Chart object or a dictionary with chart properties.

        Parameters:
            value (Chart | dict): The new chart object or a dictionary to create/update the chart.
        """
        if isinstance(value, Chart):
            self._chart = value
        elif isinstance(value, dict):
            # Update or create a new Chart object from dictionary
            self._chart = Chart.from_dict(value)
        else:
            raise TypeError("Chart must be a Chart object or a dictionary of chart properties.")
        
    @legend.setter
    def legend(self, value):
        """
        Sets the legend. The value can be a Legend object or a dictionary with chart properties.

        Parameters:
            value (Legend | dict): The new legend object or a dictionary to create/update the legend.
        """
        if isinstance(value, Legend):
            self._legend = value
        elif isinstance(value, dict):
            # Update or create a new Chart object from dictionary
            self._legend = Legend.from_dict(value)
        else:
            raise TypeError("Chart must be a Chart object or a dictionary of chart properties.")

    def set_x_axis(self,**kwargs):
        if self._x_axis is None:
           self._x_axis = XAxis(**kwargs)

    def set_legend(self,**kwargs):
        if self._legend is None:
           self._legend = Legend(**kwargs)

    def set_chart(self,**kwargs):
        if self._chart is None:
           self._chart = Chart(**kwargs)
    
    def set_title(self,**kwargs):
        if self._title is None:
           self._title = Title(**kwargs)

    def set_subtitle(self,**kwargs):
        if self._subtitle is None:
           self._subtitle = Subtitle(**kwargs)

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

    def add_series_from_dataframe(self, dataframe, column_name, series_name, **kwargs):
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

    def add_y_axis(self):
        pass

    def set_x_axis(self):
        pass

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
    
    def apply_template(self, template:dict=None):
        """
        Applies a template to the chart. The template should be a dictionary with possible keys
        for 'title', 'subtitle', and 'series', each containing further settings.

        Args:
            template (dict): A dictionary containing the chart configuration.
        """

        if 'chart' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.chart = Chart.from_dict(template['chart'])

        if 'title' in template:
            # Assumes Title has a from_dict class method or similar functionality
            self.title = Title.from_dict(template['title'])
        
        if 'subtitle' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.subtitle = Subtitle.from_dict(template['subtitle'])

        if 'legend' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self.legend = Legend.from_dict(template['legend'])

        if 'xAxis' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._x_axis = XAxis.from_dict(template['xAxis'])

        if 'yAxis' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._y_axis = YAxis.from_dict(template['yAxis'])

        if 'plotOptions' in template:
            # Assumes Subtitle has a from_dict class method or similar functionality
            self._plot_options = PlotOptions.from_dict(template['plotOptions'])

        if 'series' in template:
            # Clear existing series and add new ones from the template
            # self.series.clear()
            # for serie_data in template['series']:
            #     # Assumes Series has a from_dict class method or similar functionality
            #     self.series.append(Series.from_dict(serie_data))
            pass

    def render(self):
        """
        Generates a dictionary representation of the chart object, including only available components.

        Returns:
            dict: A dictionary with keys for 'chart', 'title', 'subtitle', and 'series' if they exist.
        """
        result = {}
        if self._chart:
            result['chart'] = self._chart.to_dict()
        if self._title:
            result['title'] = self._title.to_dict()
        if self._subtitle:
            result['subtitle'] = self._subtitle.to_dict()
        if self._legend:
            result['legend'] = self._legend.to_dict()
        if self._series:
            result['series'] = [serie.to_dict() for serie in self._series]
        
        return result