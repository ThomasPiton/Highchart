# highchart.py
from components import *
from templates import DEFAULT_TEMPLATE
from container import Container
import warnings

class Highchart(Container):
    """ 
    """
    def __init__(self):
        super().__init__()
        self.__init_default_template()
        
    def __init_default_template(self):
        """
        Initializes the chart with default settings for various components.
        These settings are typically general defaults that make the chart immediately useful.
        """
        self.chart = Chart(type='line')
        self.tooltip = Tooltip(enabled=False, shared=False, crosshairs=False)
        self.title = Title(text='Default Title', align='center')
        self.subtitle = Subtitle(text='Default Subtitle', align='center')
        self.legend = Legend(enabled=True, layout='vertical', align='left', verticalAlign='middle')
        self.plot_options = PlotOptions(series={"borderWidth": 0,"dataLabels": {"enabled": True,"format": "{point.y:.1f}%"}})

    def __set_attributes(self, component_attr, component_class, to_keep:bool=True, *args, **kwargs):
        """
        Generic method to set or update components of the Highchart.

        Args:
            component_attr (str): The attribute name of the component (e.g., "_chart", "_title").
            component_class (type): The class of the component to be instantiated (e.g., Chart, Title).
            *args: Positional arguments required by the component.
            **kwargs: Keyword arguments for the component properties.
        """
        
        component = getattr(self, component_attr, None)

        if component is None or to_keep is False:
            # If the component doesn't exist, create a new instance
            setattr(self, component_attr, component_class(*args, **kwargs))
        else:
            # If the component exists, retrieve current attributes and update with kwargs
            current_attrs = {attr: getattr(component, attr) for attr in component._valid_attributes if hasattr(component, attr)}
            # Filter kwargs to exclude None values before updating
            filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
            # Update current attributes with filtered new attributes
            current_attrs.update(filtered_kwargs)
            # Re-instantiate the component with updated attributes
            setattr(self, component_attr, component_class(**current_attrs))

    def set_legend(self,enable:bool=True,align:str=None,title:str=None,**kwargs):
        kwargs.update({"enable": enable,"align":align,"title":title})
        self.__set_attributes("_legend", Legend, **kwargs)

    def set_chart(
            self,
            type:str=None,
            to_keep:bool=True, 
            **kwargs):
        
        kwargs.update(
            {
                "type": type
            }
        )

        self.__set_attributes(component_attr="_chart", component_class=Chart, to_keep=to_keep, **kwargs)

    def set_data(
            self,
            table:str=None,
            to_keep:bool=True, 
            **kwargs):
        
        kwargs.update(
            {
                "table": table
            }
        )

        self.__set_attributes(component_attr="_data", component_class=Data, to_keep=to_keep, **kwargs)

    def set_title(
            self,
            text:str=None, 
            align:str=None,
            to_keep:bool=True, 
            **kwargs):
        
        kwargs.update(
            {
                "text": text, 
                "align": align
            }
        )

        self.__set_attributes(component_attr="_title",component_class=Title,to_keep=to_keep,**kwargs)

    def set_subtitle(
            self,
            text:str=None, 
            align:str=None,
            to_keep:bool=True, 
            **kwargs):
        
        kwargs.update(
            {
                "text": text, 
                "align": align
            }
        )

        self.__set_attributes(component_attr="_subtitle", component_class=Subtitle, to_keep=to_keep, **kwargs)

    def set_x_axis(
            self,
            to_keep:bool=True,
            **kwargs):
        
        kwargs.update({})

        self.__set_attributes(component_attr="_x_axis", component_class=XAxis,to_keep=to_keep, **kwargs)

    def set_y_axis(
            self,
            to_keep:bool=True,
            **kwargs):

        kwargs.update({})

        self.__set_attributes(component_attr="_y_axis", component_class=YAxis,to_keep=to_keep, **kwargs)

    def set_tooltip(
            self,
            to_keep:bool=True,
            **kwargs):
        
        kwargs.update({})

        self.__set_attributes(component_attr="_tooltip", component_class=Tooltip,to_keep=to_keep, **kwargs)

    def set_accessibility(
            self,
            description:str=None,
            to_keep:bool=True,
            **kwargs):

        kwargs.update(
            {
                "description": description
            }
        )
        self.__set_attributes(component_attr="_accessibility", component_class=Accessibility,to_keep=to_keep, **kwargs)

    def set_colors(self,colors:list,**kwargs):
        kwargs.update({"colors": colors})
        self.__set_attributes("_colors", Colors, **kwargs)

    def set_plot_options(
            self,
            series:dict=None,
            spline:dict=None,
            pie:dict=None,
            column:dict=None,
            line:dict=None,
            scatter:dict=None,
            area:dict=None,
            bar:dict=None,
            packedbubble:dict=None,
            streamgraph:dict=None,
            to_keep:bool=True,
            **kwargs):
        
        kwargs.update(
            {
                "series":series,
                "spline":spline,
                "pie":pie,
                "column":column,
                "line":line,
                "scatter":scatter,
                "area":area,
                "bar":bar,
                "packedbubble":packedbubble,
                "streamgraph":streamgraph
            }
        )

        self.__set_attributes(component_attr="_plot_options", component_class=PlotOptions,to_keep=to_keep,**kwargs)

    def add_x_axis(self, type:str=None, title:dict=None, **kwargs):
        if not self._x_axis: 
            self._x_axis = []
        x_axis = XAxis(type=type,title=title,**kwargs)
        self._x_axis.append(x_axis)
    
    def add_y_axis(self, type:str=None, title:dict=None, **kwargs):
        if not self._y_axis: 
            self._y_axis = []
        y_axis = YAxis(type=type,title=title,**kwargs)
        self._y_axis.append(y_axis)

    def add_colors(self, colors:list=None, **kwargs):
        if not self._colors:
            self._colors = []
        colors = Colors(colors=colors, **kwargs)
        self._colors.append()
    
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
        
        config_mapping = {
            'chart': (Chart, 'chart'),
            'tooltip': (Tooltip, 'tooltip'),
            'title': (Title, 'title'),
            'subtitle': (Subtitle, 'subtitle'),
            'legend': (Legend, 'legend'),
            'xAxis': (XAxis, '_x_axis'),
            'yAxis': (YAxis, '_y_axis'),
            'credits': (Credits, 'credits'),
            'plotOptions': (PlotOptions, '_plot_options')
        }

        supported_keys = set(config_mapping.keys())
        input_keys = set(template.keys())
        unsupported_keys = input_keys - supported_keys

        if unsupported_keys:
            warnings.warn(f"Unsupported keys provided: {', '.join(unsupported_keys)}. These will be ignored.", UserWarning)

        for key, (class_name, attr) in config_mapping.items():
            if key in template:
                setattr(self, attr, class_name.from_dict(template[key]))

    def render(self):
        """
        Generates a dictionary representation of the properties inherited from Container.
        Does not include Highchart-specific properties in the output.
        
        Returns:
            dict: A dictionary containing the rendered properties of the Container.
        """
        result = {}
        # Iterate over attributes defined in Container
        for attribute_name in vars(Container()).keys():
            key = attribute_name[1:]  # Remove the leading underscore and use as the key
            attribute = getattr(self, attribute_name, None)
            if attribute:
                result[key] = self._process_attr(attribute)

        return result

    def _process_attr(self, obj):
        """
        Convert objects with a to_dict method, lists of objects, or dictionaries to a dictionary format.
        Raises:
            TypeError: If the object type is not supported.
        """
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        
        elif isinstance(obj, list):
            return [self._to_dict(item) for item in obj]

        elif isinstance(obj, dict):
            return obj
        
        else:
            raise TypeError(f"Unsupported type {type(obj).__name__} for rendering")
    
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

    def add_series_from_dataframe(self, dataframe, column_name, series_name, drilldown=None, **kwargs):
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