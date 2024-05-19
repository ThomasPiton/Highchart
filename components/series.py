from common import Common

class Series(Common):
    """
    Represents the series in Highcharts, encapsulating the data and options that define how
    each series is displayed and behaves within the chart.

    Attributes:
        type (str): The type of series, such as 'line', 'column', etc.
        name (str): The name of the series as shown in the legend and tooltips.
        data (list): The array of data points in the series.
        color (str): The main color of the series.
        visible (bool): Whether the series is initially visible.
        enableMouseTracking (bool): Enables or disables the mouse tracking for this series.
        linkedTo (str): Allows linking this series to another series.
        index (int): The index position of the series in the chart.
        zIndex (int): Z index of the series.
        stacking (str): Type of stacking applied to the series.
        dashStyle (str): The dash style for the graph line.
        marker (dict): Configuration for the markers of points in a series.
        tooltip (dict): Custom tooltip options for the series.
        threshold (float): The threshold, above or below which the points will have different color.
        negativeColor (str): The color for the negative part of the series.
        borderColor (str): The border color of the series.
        borderWidth (int): The width of the series border.
        animation (bool/dict): Configures the animation for drawing the series.
        step (str): Used for line and area series to create a stepped path.
        keys (list): Keys for mapping data values to specific properties.
        cursor (str): Cursor type when hovering over a point in the series.
        showInLegend (bool): Whether to display this particular series in the legend.
        events (dict): Event handlers for various actions like mouseOver.
        point (dict): Options for each individual point within the series.
        turboThreshold (int): Threshold at which point series data arrays are no longer created and point objects are created directly.
        pointStart (float): First value for the X axis in the series.
        pointInterval (float): Interval between consecutive values in the series.
        pointIntervalUnit (str): Allows setting the point interval unit.
        softThreshold (bool): Whether the series should have a soft threshold.
        connectNulls (bool): Whether to connect a graph line across null points.
        clip (bool): Whether to clip points outside the plot area.
        zones (list): Defined zones within the series.
        zoneAxis (str): Defines the axis for zones in the series.
        compare (str): Whether to compare values in the series.
        dataLabels (dict): Configuration for the data labels showing information about the data points.
        drilldown (str): ID for the associated drilldown series.
        linecap (str): The end cap style for a line series.
        states (dict): States for hover, select, and inactive conditions in series.
        shadow (bool): Whether to apply a shadow to the series.
        stackId (str): An ID for the stack in stacking series.
        grouping (bool): Whether to group this series' points visually.
        groupPadding (float): Padding between each value groups.
        pointPadding (float): Padding between each point in the series.
        groupZPadding (float): Depth of the series in 3D charts.
        dataGrouping (dict): Options for data grouping in terms of time intervals.
        pointPlacement (str/float): Where to place points in relation to categories.

    Valid attributes are stored in _valid_attributes list and checked during initialization.
    """
    
    _list_only = False
    
    _valid_attributes = [
        "type","name","data","color","visible","enableMouseTracking",
        "linkedTo","index","zIndex","stacking","dashStyle","marker",
        "tooltip","threshold","negativeColor","borderColor","borderRadius",
        "borderWidth","animation","step","keys","cursor","showInLegend",
        "events","point","turboThreshold","pointStart","pointInterval",
        "pointIntervalUnit","softThreshold","connectNulls","clip",
        "zones","zoneAxis","compare","dataLabels","drilldown","linecap",
        "states","shadow","stackId","grouping","groupPadding","pointPadding",
        "groupZPadding","dataGrouping","pointPlacement","yAxis", "colorByPoint"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        