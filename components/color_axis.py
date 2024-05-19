from common import Common

from common import Common

class ColorAxis(Common):
    """
    Represents the ColorAxis in a Highcharts chart configuration.

    Attributes:
        accessibility (dict): Configuration for accessibility.
        angle (int): The angle of the axis.
        ceiling (float): The maximum value of the axis.
        className (str): A custom class name for the axis.
        crossing (float): The crossing point of the axis.
        dataClassColor (str): The color of the data class.
        dataClasses (list): Array defining color classes.
        endOnTick (bool): Whether to end the axis on a tick.
        events (dict): Event handlers for the axis.
        floor (float): The minimum value of the axis.
        gridLineColor (str): Color of the grid lines.
        gridLineDashStyle (str): Style of the grid lines.
        gridLineInterpolation (str): The interpolation mode for the grid lines.
        gridLineWidth (int): Width of the grid lines.
        gridZIndex (int): The Z-index of the grid lines.
        height (int): The height of the axis.
        id (str): An ID for the axis.
        labels (dict): Labels for the axis.
        layout (str): Layout of the axis.
        lineColor (str): Color of the axis line.
        margin (int): Margin of the axis.
        marker (dict): Marker configuration for the axis.
        max (float): Maximum value of the axis.
        maxColor (str): Color for the maximum end of the gradient.
        maxPadding (float): Padding for the maximum value.
        min (float): Minimum value of the axis.
        minColor (str): Color for the minimum end of the gradient.
        minorGridLineColor (str): Color of the minor grid lines.
        minorGridLineDashStyle (str): Style of the minor grid lines.
        minorGridLineWidth (int): Width of the minor grid lines.
        minorTickColor (str): Color of the minor ticks.
        minorTickInterval (float): Interval between minor ticks.
        minorTickLength (int): Length of the minor ticks.
        minorTickPosition (str): Position of the minor ticks.
        minorTicks (bool): Whether to show minor ticks.
        minorTicksPerMajor (int): Number of minor ticks per major tick.
        minorTickWidth (int): Width of the minor ticks.
        minPadding (float): Padding for the minimum value.
        panningEnabled (bool): Whether panning is enabled.
        reversed (bool): Whether to reverse the axis.
        showFirstLabel (bool): Whether to show the first label.
        showInLegend (bool): Whether to show the axis in the legend.
        showLastLabel (bool): Whether to show the last label.
        softMax (float): Soft maximum value of the axis.
        softMin (float): Soft minimum value of the axis.
        startOfWeek (int): The starting day of the week.
        startOnTick (bool): Whether to start the axis on a tick.
        stops (list): Array of color stops for the gradient.
        tickAmount (int): Amount of ticks on the axis.
        tickColor (str): Color of the ticks.
        tickInterval (float): Interval between ticks.
        tickLength (int): Length of the ticks.
        tickmarkPlacement (str): Placement of the tick marks.
        tickPixelInterval (int): Pixel interval between ticks.
        tickPosition (str): Position of the ticks.
        tickPositioner (func): Custom function for tick positions.
        tickPositions (list): Custom tick positions.
        tickWidth (int): Width of the ticks.
        type (str): Type of axis, e.g., 'linear' or 'logarithmic'.
        uniqueNames (bool): Whether to use unique names.
        units (list): Units for the axis.
        visible (bool): Visibility of the axis.
        width (int): Width of the axis.
        zIndex (int): Z-index of the axis.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'accessibility', 'angle', 'ceiling', 'className', 'crossing', 
        'dataClassColor', 'dataClasses', 'endOnTick', 'events', 'floor', 
        'gridLineColor', 'gridLineDashStyle', 'gridLineInterpolation', 
        'gridLineWidth', 'gridZIndex', 'height', 'id', 'labels', 'layout', 
        'lineColor', 'margin', 'marker', 'max', 'maxColor', 'maxPadding', 
        'min', 'minColor', 'minorGridLineColor', 'minorGridLineDashStyle', 
        'minorGridLineWidth', 'minorTickColor', 'minorTickInterval', 
        'minorTickLength', 'minorTickPosition', 'minorTicks', 
        'minorTicksPerMajor', 'minorTickWidth', 'minPadding', 'panningEnabled', 
        'reversed', 'showFirstLabel', 'showInLegend', 'showLastLabel', 
        'softMax', 'softMin', 'startOfWeek', 'startOnTick', 'stops', 
        'tickAmount', 'tickColor', 'tickInterval', 'tickLength', 
        'tickmarkPlacement', 'tickPixelInterval', 'tickPosition', 
        'tickPositioner', 'tickPositions', 'tickWidth', 'type', 'uniqueNames', 
        'units', 'visible', 'width', 'zIndex'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the ColorAxis with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
