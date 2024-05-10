# chart.py

from common import Common

class Chart(Common):
    """
    Represents the main chart settings in Highcharts, allowing for detailed
    customization of the chart's appearance and behavior.

    Attributes:
        type (str): Specifies the default series type for the chart.
        alignTicks (bool): Whether to align ticks of different axes regarding each other.
        animation (bool/dict): Controls the animation of the initial series and redraws.
        backgroundColor (str): The background color of the chart.
        borderColor (str): The color of the border surrounding the chart.
        borderRadius (int): The corner radius of the border surrounding the chart.
        borderWidth (int): The width of the border surrounding the chart.
        className (str): A custom class name to apply to the chart container.
        colorCount (int): The number of colors in the default color palette.
        defaultSeriesType (str): Alias for type.
        displayErrors (bool): Whether to display errors in the chart.
        events (dict): Event handlers for the chart.
        height (int): The height of the chart.
        ignoreHiddenSeries (bool): Whether to ignore hidden series when laying out the chart.
        inverted (bool): Whether to invert the axes so that the x-axis appears vertical.
        margin (int/list): The space around the outside of the chart.
        marginTop (int): Top margin of the chart.
        marginRight (int): Right margin of the chart.
        marginBottom (int): Bottom margin of the chart.
        marginLeft (int): Left margin of the chart.
        options3d (dict): Options for a 3D appearance of some charts.
        panKey (str): Which key must be pressed to allow panning.
        panning (bool): Allows panning the chart using the mouse.
        pinchType (str): Specifies the type of pinch gesture needed to zoom or pan.
        plotBackgroundColor (str): The background color of the plot area.
        plotBackgroundImage (str): An image to use as the plot area background.
        plotBorderColor (str): The color of the border around the plot area.
        plotBorderWidth (int): The width of the border around the plot area.
        plotShadow (bool): Whether to apply a drop shadow to the plot area.
        polar (bool): Whether to display the chart as a polar chart.
        reflow (bool): Whether to reflow the chart to fit the width of the container on resizing.
        renderTo (str): The HTML element ID where the chart should render.
        resetZoomButton (dict): Configuration for the button that resets zoom.
        selectionMarkerFill (str): The fill color for the selection marker box.
        shadow (bool): Whether to apply a shadow to the main chart area.
        showAxes (bool): Display the axes when the chart is first drawn.
        spacing (int): The spacing around the outside of the chart.
        spacingTop (int): Top spacing of the chart.
        spacingRight (int): Right spacing of the chart.
        spacingBottom (int): Bottom spacing of the chart.
        spacingLeft (int): Left spacing of the chart.
        style (dict): CSS for the entire chart container.
        styledMode (bool): Whether to style by CSS.
        typeDescription (str): Description of the chart type, used for accessibility.
        width (int): The width of the chart.
        zoomType (str): Defines the dimensions that can be zoomed using a mouse drag.
        zoomKey (str): Defines a key to hold down to allow zooming.

    Valid attributes are stored in _valid_attributes list and checked during initialization.
    """
    
    _valid_chart_type = [
        "series","spline","pie","column","line","areaspline","arearange","columnrange",
        "scatter","area","bar","packedbubble","streamgraph","variwide","variablepie"
    ]

    _valid_attributes = [
        "type","alignTicks","animation","backgroundColor","borderColor","borderRadius",
        "borderWidth","className","colorCount","defaultSeriesType","displayErrors","events",
        "height","ignoreHiddenSeries","inverted","margin","marginTop","marginRight","marginBottom",
        "marginLeft","options3d","panKey","panning","pinchType","plotBackgroundColor",
        "plotBackgroundImage","plotBorderColor","plotBorderWidth","plotShadow","polar",
        "reflow","renderTo","resetZoomButton","selectionMarkerFill","shadow","showAxes",
        "spacing","spacingTop","spacingRight","spacingBottom","spacingLeft","style",
        "styledMode","typeDescription","width","zoomType","zoomKey"]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)


# ======================================================================================================================

# class Chart:

#     # A list of all valid attributes for the Chart class
#     _valid_attributes = [
#         'chart_type', 'background_color', 'border_color', 'border_radius',
#         'border_width', 'color_count', 'display_errors', 'height', 'inverted',
#         'margin', 'options_3d', 'panning', 'pan_key', 'plot_background_color',
#         'plot_border_color', 'plot_border_width', 'plot_shadow', 'polar', 'reflow',
#         'render_to', 'reset_zoom_button', 'selection_marker_fill', 'shadow',
#         'show_axes', 'spacing', 'styled_mode', 'width', 'zoom_type'
#     ]

#     def __init__(self, **kwargs):
#         # Initialize all attributes to None or their default values
#         self.__dict__.update({attr: None for attr in self._valid_attributes})
#         # Update the attributes with any values provided upon instantiation
#         self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

#     def to_dict(self):
#         """
#         Converts the Chart object into a dictionary suitable for configurations.

#         Returns:
#             dict: A dictionary representing the chart configuration.
#         """
#         return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}
    
#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Chart object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the chart.

#         Returns:
#             Chart: A Chart object configured according to the provided dictionary.
#         """
#         return cls(**{k: v for k, v in data.items() if k in cls._valid_attributes})

# ======================================================================================================================

# from dataclasses import dataclass, field

# @dataclass
# class Chart:

#     # Dynamic attributes are stored in a dictionary
#     attributes: dict = field(default_factory=dict)

#     # A list of all valid attributes for the Chart class
#     _valid_attributes = [
#         'chart_type', 'background_color', 'border_color', 'border_radius',
#         'border_width', 'color_count', 'display_errors', 'height', 'inverted',
#         'margin', 'options_3d', 'panning', 'pan_key', 'plot_background_color',
#         'plot_border_color', 'plot_border_width', 'plot_shadow', 'polar', 'reflow',
#         'render_to', 'reset_zoom_button', 'selection_marker_fill', 'shadow',
#         'show_axes', 'spacing', 'styled_mode', 'width', 'zoom_type'
#     ]

#     def __post_init__(self):
#         # Validate keys and handle attributes initialization
#         extra_keys = set(self.attributes.keys()) - set(self._valid_attributes)
#         if extra_keys:
#             raise ValueError(f"Invalid attribute keys passed: {extra_keys}")
#         self.attributes = {k: v for k, v in self.attributes.items() if k in self._valid_attributes}

#     def to_dict(self):
#         """
#         Converts the Chart object into a dictionary suitable for configurations.

#         Returns:
#             dict: A dictionary representing the chart configuration.
#         """
#         return {attr: value for attr, value in self.attributes.items() if value is not None}

#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Chart object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the chart.

#         Returns:
#             Chart: A Chart object configured according to the provided dictionary.
#         """
#         return cls(attributes={k: data[k] for k in cls._valid_attributes if k in data})
