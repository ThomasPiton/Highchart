from common import Common

class YAxis(Common):
    """
    Represents the Y-axis of the chart, allowing for detailed customization
    of the axis properties.

    Attributes:
        accessibility (dict or None): Accessibility options for the axis.
        alignTicks (bool): Whether to align ticks.
        allowDecimals (bool or None): Whether to allow decimals in the axis values.
        alternateGridColor (str or None): Color for alternate grid bands.
        angle (int): The angle of the axis labels.
        breaks (list or None): Breaks in the axis.
        categories (list or None): Categories for the axis.
        ceiling (int or None): The maximum value of the axis.
        className (str or None): A custom class name for the axis.
        crosshair (dict or None): Crosshair options for the axis.
        crossing (int or None): The crossing point of another axis.
        dateTimeLabelFormats (dict or None): Date-time label formats for the axis.
        endOnTick (bool): Whether to end the axis on a tick.
        events (dict or None): Event handlers for the axis.
        floor (int or None): The minimum value of the axis.
        gridLineColor (str): The color of the grid lines.
        gridLineDashStyle (str): The dash style of the grid lines.
        gridLineInterpolation (str or None): The interpolation of the grid lines.
        gridLineWidth (int): The width of the grid lines.
        gridZIndex (int): The Z-index of the grid lines.
        height (int or None): The height of the axis.
        id (str or None): An ID for the axis.
        labels (dict or None): Label options for the axis.
        left (int or None): The left position of the axis.
        lineColor (str): The color of the axis line.
        lineWidth (int): The width of the axis line.
        linkedTo (int or None): The index of another axis to link to.
        margin (int or None): The margin of the axis.
        max (int or None): The maximum value of the axis.
        maxColor (str): The color for the maximum value.
        maxPadding (float): The maximum padding of the axis.
        maxZoom (int or None): The maximum zoom level of the axis.
        min (int or None): The minimum value of the axis.
        minColor (str): The color for the minimum value.
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
        reversed (bool): Whether to reverse the axis.
        reversedStacks (bool): Whether to reverse stacks.
        showEmpty (bool): Whether to show the axis if it's empty.
        showFirstLabel (bool): Whether to show the first label.
        showLastLabel (bool or None): Whether to show the last label.
        softMax (int or None): A soft maximum for the axis.
        softMin (int or None): A soft minimum for the axis.
        stackLabels (dict or None): Options for the stack labels.
        stackShadow (bool or None): Whether to apply shadow to the stack labels.
        startOfWeek (int): The start day of the week.
        startOnTick (bool): Whether to start the axis on a tick.
        stops (list or None): Stops for the axis gradient.
        tickAmount (int or None): The amount of ticks.
        tickColor (str): The color of the ticks.
        tickInterval (int or None): The interval of the ticks.
        tickLength (int): The length of the ticks.
        tickmarkPlacement (str): The placement of the tick marks.
        tickPixelInterval (int): The pixel interval of the ticks.
        tickPosition (str): The position of the ticks.
        tickPositioner (func or None): A custom tick positioner function.
        tickPositions (list or None): The positions of the ticks.
        tickWidth (int): The width of the ticks.
        title (dict or None): The title options for the axis.
        tooltipValueFormat (str or None): The format for the tooltip values.
        top (int or None): The top position of the axis.
        type (str): The type of the axis.
        uniqueNames (bool): Whether to use unique names.
        units (list or None): Units for the axis.
        visible (bool): Whether the axis is visible.
        width (int or None): The width of the axis.
        zIndex (int): The Z-index of the axis.
        zoomEnabled (bool): Whether zooming is enabled.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'accessibility', 'alignTicks', 'allowDecimals', 'alternateGridColor', 'angle', 'breaks',
        'categories', 'ceiling', 'className', 'crosshair', 'crossing', 'dateTimeLabelFormats',
        'endOnTick', 'events', 'floor', 'gridLineColor', 'gridLineDashStyle', 'gridLineInterpolation',
        'gridLineWidth', 'gridZIndex', 'height', 'id', 'labels', 'left', 'lineColor', 'lineWidth',
        'linkedTo', 'margin', 'max', 'maxColor', 'maxPadding', 'maxZoom', 'min', 'minColor',
        'minorGridLineColor', 'minorGridLineDashStyle', 'minorGridLineWidth', 'minorTickColor',
        'minorTickInterval', 'minorTickLength', 'minorTickPosition', 'minorTicks', 'minorTicksPerMajor',
        'minorTickWidth', 'minPadding', 'minRange', 'minTickInterval', 'offset', 'opposite', 'pane',
        'panningEnabled', 'plotBands', 'plotLines', 'reversed', 'reversedStacks', 'showEmpty',
        'showFirstLabel', 'showLastLabel', 'softMax', 'softMin', 'stackLabels', 'stackShadow',
        'startOfWeek', 'startOnTick', 'stops', 'tickAmount', 'tickColor', 'tickInterval', 'tickLength',
        'tickmarkPlacement', 'tickPixelInterval', 'tickPosition', 'tickPositioner', 'tickPositions',
        'tickWidth', 'title', 'tooltipValueFormat', 'top', 'type', 'uniqueNames', 'units', 'visible',
        'width', 'zIndex', 'zoomEnabled'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the YAxis options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
