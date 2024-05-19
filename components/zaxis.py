from common import Common

from common import Common

class ZAxis(Common):
    """
    Represents the Z-axis of the chart, allowing for detailed customization
    of the axis properties.

    Attributes:
        accessibility (dict or None): Accessibility options for the axis.
        alignTicks (bool): Whether to align ticks.
        allowDecimals (bool or None): Whether to allow decimals in the axis values.
        alternateGridColor (str or None): Color for alternate grid bands.
        angle (int): The angle of the axis labels.
        categories (list or None): Categories for the axis.
        ceiling (int or None): The maximum value of the axis.
        className (str or None): A custom class name for the axis.
        crossing (int or None): The crossing point of another axis.
        dateTimeLabelFormats (dict or None): Date-time label formats for the axis.
        endOnTick (bool): Whether to end the axis on a tick.
        events (dict or None): Event handlers for the axis.
        floor (int or None): The minimum value of the axis.
        gridLineColor (str): The color of the grid lines.
        gridLineDashStyle (str): The dash style of the grid lines.
        gridLineInterpolation (str or None): The interpolation of the grid lines.
        gridLineWidth (int or None): The width of the grid lines.
        gridZIndex (int): The Z-index of the grid lines.
        id (str or None): An ID for the axis.
        labels (dict or None): Label options for the axis.
        linkedTo (int or None): The index of another axis to link to.
        margin (int or None): The margin of the axis.
        max (int or None): The maximum value of the axis.
        maxPadding (float): The maximum padding of the axis.
        maxZoom (int or None): The maximum zoom level of the axis.
        min (int or None): The minimum value of the axis.
        minorGridLineColor (str): The color of the minor grid lines.
        minorGridLineDashStyle (str): The dash style of the minor grid lines.
        minorGridLineWidth (int): The width of the minor grid lines.
        minorTickColor (str): The color of the minor ticks.
        minorTickInterval (float or None): The interval of the minor ticks.
        minorTickLength (int): The length of the minor ticks.
        minorTickPosition (str): The position of the minor ticks.
        minorTicks (bool): Whether to show minor ticks.
        minorTicksPerMajor (int): The number of minor ticks per major tick.
        minorTickWidth (int): The width of the minor ticks.
        minPadding (float): The minimum padding of the axis.
        minRange (int or None): The minimum range of the axis.
        minTickInterval (float or None): The minimum tick interval.
        offset (int or None): The offset of the axis.
        opposite (bool): Whether to position the axis on the opposite side.
        pane (int or None): The pane to which the axis belongs.
        panningEnabled (bool): Whether panning is enabled.
        plotBands (list or None): Plot bands for the axis.
        plotLines (list or None): Plot lines for the axis.
        reversed (bool or None): Whether to reverse the axis.
        reversedStacks (bool): Whether to reverse stacks.
        showFirstLabel (bool): Whether to show the first label.
        showLastLabel (bool or None): Whether to show the last label.
        softMax (int or None): A soft maximum for the axis.
        softMin (int or None): A soft minimum for the axis.
        startOfWeek (int): The start day of the week.
        startOnTick (bool): Whether to start the axis on a tick.
        tickAmount (int or None): The amount of ticks.
        tickColor (str): The color of the ticks.
        tickInterval (int or None): The interval of the ticks.
        tickLength (int): The length of the ticks.
        tickmarkPlacement (str): The placement of the tick marks.
        tickPixelInterval (int): The pixel interval of the ticks.
        tickPosition (str): The position of the ticks.
        tickPositioner (func or None): A custom tick positioner function.
        tickPositions (list or None): The positions of the ticks.
        tickWidth (int or None): The width of the ticks.
        title (dict or None): The title options for the axis.
        type (str): The type of the axis.
        uniqueNames (bool): Whether to use unique names.
        units (list or None): Units for the axis.
        visible (bool): Whether the axis is visible.
        zIndex (int): The Z-index of the axis.
        zoomEnabled (bool): Whether zooming is enabled.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'accessibility', 'alignTicks', 'allowDecimals', 'alternateGridColor', 'angle', 'categories',
        'ceiling', 'className', 'crossing', 'dateTimeLabelFormats', 'endOnTick', 'events', 'floor',
        'gridLineColor', 'gridLineDashStyle', 'gridLineInterpolation', 'gridLineWidth', 'gridZIndex',
        'id', 'labels', 'linkedTo', 'margin', 'max', 'maxPadding', 'maxZoom', 'min', 'minorGridLineColor',
        'minorGridLineDashStyle', 'minorGridLineWidth', 'minorTickColor', 'minorTickInterval',
        'minorTickLength', 'minorTickPosition', 'minorTicks', 'minorTicksPerMajor', 'minorTickWidth',
        'minPadding', 'minRange', 'minTickInterval', 'offset', 'opposite', 'pane', 'panningEnabled',
        'plotBands', 'plotLines', 'reversed', 'reversedStacks', 'showFirstLabel', 'showLastLabel',
        'softMax', 'softMin', 'startOfWeek', 'startOnTick', 'tickAmount', 'tickColor', 'tickInterval',
        'tickLength', 'tickmarkPlacement', 'tickPixelInterval', 'tickPosition', 'tickPositioner',
        'tickPositions', 'tickWidth', 'title', 'type', 'uniqueNames', 'units', 'visible', 'zIndex',
        'zoomEnabled'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the ZAxis options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
