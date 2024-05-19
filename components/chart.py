# chart.py
from common import Common

class Chart(Common):
    """
    Represents the chart options for a Highcharts chart configuration.

    Attributes:
        alignThresholds (bool): Whether to align thresholds.
        alignTicks (bool): Whether to align ticks.
        allowMutatingData (bool): Whether to allow mutating data.
        animation (bool or dict): Whether to enable animation.
        axisLayoutRuns (int): Number of axis layout runs.
        backgroundColor (str): Background color of the chart.
        borderColor (str): Border color of the chart.
        borderRadius (int): Border radius of the chart.
        borderWidth (int): Border width of the chart.
        className (str): A class name for the chart container.
        colorCount (int): The number of colors in the default color palette.
        displayErrors (bool): Whether to display errors.
        events (dict): Event handlers for the chart.
        height (int or None): Height of the chart.
        ignoreHiddenSeries (bool): Whether to ignore hidden series.
        inverted (bool): Whether to invert the chart.
        margin (list or None): The margin around the chart.
        marginBottom (int or None): The bottom margin of the chart.
        marginLeft (int or None): The left margin of the chart.
        marginRight (int or None): The right margin of the chart.
        marginTop (int or None): The top margin of the chart.
        numberFormatter (func or None): Custom number formatter function.
        options3d (dict): 3D options for the chart.
        panKey (str or None): The key to hold to enable panning.
        panning (dict): Panning options for the chart.
        parallelAxes (dict): Parallel axes configuration.
        parallelCoordinates (bool): Whether to enable parallel coordinates.
        pinchType (str or None): The type of pinch gestures.
        plotBackgroundColor (str or None): Background color for the plot area.
        plotBackgroundImage (str or None): Background image for the plot area.
        plotBorderColor (str): Border color for the plot area.
        plotBorderWidth (int): Border width for the plot area.
        plotShadow (bool or dict): Shadow options for the plot area.
        polar (bool): Whether to enable polar charts.
        reflow (bool): Whether to reflow the chart on window resize.
        renderTo (str or None): The HTML element ID to render the chart to.
        resetZoomButton (dict): Options for the reset zoom button.
        scrollablePlotArea (dict): Scrollable plot area options.
        selectionMarkerFill (str): Fill color for the selection marker.
        shadow (bool or dict): Shadow options for the chart.
        showAxes (bool or None): Whether to show axes initially.
        spacing (list): The spacing around the chart.
        spacingBottom (int): The bottom spacing of the chart.
        spacingLeft (int): The left spacing of the chart.
        spacingRight (int): The right spacing of the chart.
        spacingTop (int): The top spacing of the chart.
        style (dict): CSS styles for the chart.
        styledMode (bool): Whether to use styled mode.
        type (str): The default series type.
        width (int or None): Width of the chart.
        zooming (dict): Zooming options for the chart.
        zoomKey (str or None): The key to hold to enable zooming.
        zoomType (str or None): The type of zoom gestures.
    """
    
    _list_only = False
    
    _valid_chart_type = [
        "series","spline","pie","column","line","areaspline","arearange","columnrange",
        "scatter","area","bar","packedbubble","streamgraph","variwide","variablepie"
    ]

    _valid_attributes = [
        'alignThresholds', 'alignTicks', 'allowMutatingData', 'animation', 
        'axisLayoutRuns', 'backgroundColor', 'borderColor', 'borderRadius', 
        'borderWidth', 'className', 'colorCount', 'displayErrors', 'events', 
        'height', 'ignoreHiddenSeries', 'inverted', 'margin', 'marginBottom', 
        'marginLeft', 'marginRight', 'marginTop', 'numberFormatter', 
        'options3d', 'panKey', 'panning', 'parallelAxes', 'parallelCoordinates', 
        'pinchType', 'plotBackgroundColor', 'plotBackgroundImage', 
        'plotBorderColor', 'plotBorderWidth', 'plotShadow', 'polar', 'reflow', 
        'renderTo', 'resetZoomButton', 'scrollablePlotArea', 'selectionMarkerFill', 
        'shadow', 'showAxes', 'spacing', 'spacingBottom', 'spacingLeft', 
        'spacingRight', 'spacingTop', 'style', 'styledMode', 'type', 'width', 
        'zooming', 'zoomKey', 'zoomType'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Chart options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)


