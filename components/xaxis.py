
from common import Common

class XAxis(Common):
    """
    Represents the X-axis of a Highcharts chart, providing extensive configuration options
    that define the behavior and appearance of the x-axis in a chart.

    Attributes:
        _valid_attributes (list): A list of all valid attributes for the X-axis configuration. 
        These attributes can control various aspects such as axis limits, grid lines, labels, 
        tick marks, and other axis-related properties.

    Valid Attributes Include:
        - allowDecimals (bool): Whether to allow decimals in this axis' labels.
        - alternateGridColor (str): Color for the alternate grid bands.
        - categories (list): If categories are present for the axis, names are used instead of numbers for the axis.
        - ceiling (float): Maximum value of the axis.
        - className (str): CSS class names for styling the axis.
        - crosshair (dict): Configure the crosshair line that follows the cursor.
        - dateTimeLabelFormats (dict): For axes with datetime type, format of the date/time label.
        - endOnTick (bool): Whether to force the axis to end on a tick.
        - events (dict): Event handlers for the axis events.
        - floor (float): Minimum value of the axis.
        - gridLineColor (str): Color of the grid lines along the axis.
        - gridLineDashStyle (str): Dash style of the grid lines.
        - gridLineWidth (int): Width of the grid lines.
        - gridZIndex (int): The Z index of the grid lines.
        - id (str): An unique identifier for the axis.
        - labels (dict): Configuration for the axis labels.
        - lineColor (str): Color of the line of the axis.
        - lineWidth (int): Width of the line of the axis.
        - linkedTo (int): The index of another axis that this axis is linked to.
        - max (float): The maximum value of the axis.
        - maxLength (int): Maximum pixel length of the axis.
        - min (float): The minimum value of the axis.
        - minPadding (float): Padding of the minimum range of the axis.
        - minRange (float): The minimum range to be displayed.
        - minTickInterval (int): The minimum interval between ticks.
        - minorGridLineColor (str): Color of the minor grid lines.
        - minorGridLineDashStyle (str): Dash style of the minor grid lines.
        - minorGridLineWidth (int): Width of the minor grid lines.
        - minorTickColor (str): Color of the minor ticks.
        - minorTickInterval (var): The interval of the minor ticks.
        - minorTickLength (int): The length of the minor ticks.
        - minorTickPosition (str): Position of the minor ticks relative to the axis line.
        - minorTickWidth (int): Width of the minor ticks.
        - offset (int): The offset of the axis from the chart area.
        - opposite (bool): Whether to display the axis on the opposite side of the default.
        - plotBands (list): Array of objects to configure plot bands.
        - plotLines (list): Array of objects to configure plot lines.
        - reversed (bool): Whether to reverse the axis direction.
        - showEmpty (bool): Whether to display the axis line and title when there are no data points.
        - showFirstLabel (bool): Whether to show the first label on the axis.
        - showLastLabel (bool): Whether to show the last label on the axis.
        - startOfWeek (int): For datetime axes, this decides the start day of the week. Default is Monday.
        - startOnTick (bool): Whether to force the axis to start on a tick.
        - tickAmount (int): The exact number of ticks to be shown on the axis.
        - tickColor (str): Color of the ticks.
        - tickInterval (int): The interval of the ticks in axis units.
        - tickLength (int): The length of the ticks in pixels.
        - tickPixelInterval (int): If tickInterval is not set, this defines the approximate pixel interval of the ticks.
        - tickPosition (str): Position of the ticks relative to the axis line.
        - tickPositioner (function): A function to position the ticks.
        - tickPositions (list): A predefined list of tick positions.
        - tickWidth (int): Width of the ticks.
        - tickmarkPlacement (str): Specifies how the ticks are laid out when the axis is a category axis.
        - title (dict): Configuration for the axis title.
        - type (str): Specifies the type of the axis.
        - uniqueNames (bool): Whether to ensure that each category name is unique.
        - units (list): Multiple time units for datetime axes.
    """

    _valid_attributes = [
        "allowDecimals","alternateGridColor","categories","ceiling",
        "className","crosshair","dateTimeLabelFormats","endOnTick","events","floor",
        "gridLineColor","gridLineDashStyle","gridLineWidth","gridZIndex","id","labels",
        "lineColor","lineWidth","linkedTo","max","maxLength","min","minPadding","minRange",
        "minTickInterval","minorGridLineColor","minorGridLineDashStyle","minorGridLineWidth",
        "minorTickColor","minorTickInterval","minorTickLength","minorTickPosition","minorTickWidth",
        "offset","opposite","plotBands","plotLines","reversed","showEmpty","showFirstLabel",
        "showLastLabel","startOfWeek","startOnTick","tickAmount","tickColor","tickInterval",
        "tickLength","tickPixelInterval","tickPosition","tickPositioner","tickPositions",
        "tickWidth","tickmarkPlacement","title","type","uniqueNames","units"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)