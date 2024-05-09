# plot_options.py

from chart_component import ChartComponent

class PlotOptions(ChartComponent):
    """
    Represents the plot options in Highcharts, allowing for detailed
    customization of the plotting behavior and visual style across different series types.

    Attributes:
        allowPointSelect (bool): Allows points in the series to be selected by clicking.
        animation (bool/dict): Configures the animation for plotting points.
        className (str): A custom class name to attach to the series' graphical elements.
        colorIndex (int): The color index of the series.
        colors (list): An array of colors for the points in the series.
        connectEnds (bool): Whether to connect the ends of a series in a closed shape.
        connectNulls (bool): Whether to connect a graph line across null points.
        cropThreshold (int): The number of points after which a series is cropped.
        cursor (str): Cursor type to be displayed when pointing on a graph.
        dashStyle (str): The dash style for the graph.
        dataGrouping (dict): Options for data grouping in terms of time intervals.
        dataLabels (dict): Options for displaying labels on data points.
        depth (int): Depth of the series (useful in 3D charts).
        enableMouseTracking (bool): Whether to enable mouse tracking for a series.
        exposeElementToA11y (bool): Whether to expose the series to accessibility features.
        findNearestPointBy (str): Determines how the tooltip finds points.
        getExtremesFromAll (bool): Whether to calculate extremes from all data points.
        ignoreHiddenPoint (bool): Whether to ignore hidden points when drawing.
        inactive (dict): Style settings for inactive (unhovered) series.
        index (int): An optional zIndex of the series.
        innerSize (str/int): The inner size of a pie chart series.
        keys (list): Specifies what keys to use for each data point array.
        label (dict): Options for a data label per series.
        linkedTo (str): Linking this series to another series.
        minSize (int): Minimum size for a pie chart series.
        point (dict): Options for each individual point within the series.
        pointDescriptionFormatter (func): Formatter for point descriptions.
        pointInterval (int): The interval between points on the X-axis.
        pointIntervalUnit (str): Allows setting the point interval unit.
        pointPadding (float): Padding between each point in the series.
        pointPlacement (str/float): Where to place points in relation to categories.
        pointRange (int): The range of the points.
        pointStart (int): The starting point in X-axis data.
        pointWidth (int): The fixed width of each point on the X-axis.
        selected (bool): Whether the series is selected initially.
        shadow (bool): Whether to apply a shadow to the series.
        showCheckbox (bool): Whether to show a checkbox next to the series' name in the legend.
        showInLegend (bool): Whether the series should show in the legend.
        size (int/str): The size of the series elements.
        skipKeyboardNavigation (bool): Whether to skip keyboard navigation for this series.
        stacking (str): Type of stacking for the series.
        states (dict): States for hover, select in the series.
        stickyTracking (bool): Whether to stick on hovering points.
        threshold (int): The threshold value for negative color change.
        tooltip (dict): Custom tooltip options for the series.
        turboThreshold (int): Threshold at which point series data arrays are no longer created.
        visible (bool): Whether the series is visible initially.
        zoneAxis (str): Specifies the axis for defining zones.
        zones (list): Allows defining zones within the series.

    Valid attributes are stored in _valid_attributes list and checked during initialization.
    """
    _valid_attributes = [
        "allowPointSelect","animation","className","colorIndex","colors","connectEnds",
        "connectNulls","cropThreshold","cursor","dashStyle","dataGrouping","dataLabels",
        "depth","enableMouseTracking","exposeElementToA11y","findNearestPointBy","getExtremesFromAll",
        "ignoreHiddenPoint","inactive","index","innerSize","keys","label","linkedTo",
        "minSize","point","pointDescriptionFormatter","pointInterval","pointIntervalUnit",
        "pointPadding","pointPlacement","pointRange","pointStart","pointWidth",
        "selected","shadow","showCheckbox","showInLegend","size","skipKeyboardNavigation",
        "stacking","states","stickyTracking","threshold","tooltip","turboThreshold",
        "visible","zoneAxis","zones"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

# ======================================================================================================================

# class PlotOptions:

#     # A list of all valid attributes for the Chart class
#     _valid_attributes = [
#         "allowPointSelect","animation","className","colorIndex","colors","connectEnds",
#         "connectNulls","cropThreshold","cursor","dashStyle","dataGrouping","dataLabels",
#         "depth","enableMouseTracking","exposeElementToA11y","findNearestPointBy","getExtremesFromAll",
#         "ignoreHiddenPoint","inactive","index","innerSize","keys","label","linkedTo",
#         "minSize","point","pointDescriptionFormatter","pointInterval","pointIntervalUnit",
#         "pointPadding","pointPlacement","pointRange","pointStart","pointWidth",
#         "selected","shadow","showCheckbox","showInLegend","size","skipKeyboardNavigation",
#         "stacking","states","stickyTracking","threshold","tooltip","turboThreshold",
#         "visible","zoneAxis","zones"
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
