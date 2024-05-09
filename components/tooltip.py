
from chart_component import ChartComponent

class Tooltip(ChartComponent):
    """
    Represents a Tooltip in Highcharts, used to configure how tooltips are displayed
    when interacting with the chart. This class provides an interface to set up all 
    tooltip-specific options in a structured way.

    Attributes:
        _valid_attributes (list): A class attribute listing all valid attributes for 
        a Highcharts tooltip configuration. These attributes control various aspects
        of the tooltip's appearance and behavior.

    The valid attributes include:
        - animation (bool): Enable or disable the animation of the tooltip.
        - backgroundColor (str): Background color of the tooltip.
        - borderColor (str): Border color of the tooltip.
        - borderRadius (int): Radius of the tooltip's corners.
        - borderWidth (int): Width of the tooltip's border.
        - className (str): Custom class for additional styling.
        - crosshairs (bool/list): Enable or customize crosshairs for better alignment.
        - dateTimeLabelFormats (dict): Date/time formatting for various granularities.
        - distance (int): Pixel distance between the tooltip and the hovering point.
        - enabled (bool): Enable or disable the tooltip.
        - followPointer (bool): Tooltip follows the mouse pointer or touch.
        - followTouchMove (bool): Tooltip follows touch movement on touch devices.
        - footerFormat (str): Additional string to be appended after the main tooltip format.
        - format (str): Specific format for the tooltip.
        - headerFormat (str): HTML string for the header of the tooltip.
        - hideDelay (int): Delay in milliseconds before the tooltip hides after mouse out.
        - padding (int): Padding inside the tooltip.
        - pointFormat (str): Format of the point's data in the tooltip.
        - pointFormatter (function): Custom formatter function for the point's data.
        - shared (bool): Whether the tooltip is shared across multiple series.
        - shape (str): Shape of the tooltip ('square', 'circle', 'diamond', etc.).
        - shadow (bool): Whether the tooltip should have a shadow.
        - snap (int): Distance at which the tooltip snaps to points.
        - split (bool): Split the tooltip into separate labels for each series.
        - style (dict): CSS styles for the tooltip.
        - useHTML (bool): Use HTML to render the contents of the tooltip.
        - valueDecimals (int): Number of decimal places for numeric values.
        - valuePrefix (str): Prefix for each value in the tooltip.
        - valueSuffix (str): Suffix for each value in the tooltip.
        - xDateFormat (str): Format for the x values in the tooltip.
    """
    
    _valid_attributes = [
        'animation', 'backgroundColor', 'borderColor', 'borderRadius', 'borderWidth',
        'className', 'crosshairs', 'dateTimeLabelFormats', 'distance', 'enabled',
        'followPointer', 'followTouchMove', 'footerFormat', 'format', 'headerFormat',
        'hideDelay', 'padding', 'pointFormat', 'pointFormatter', 'shared', 'shape',
        'shadow', 'snap', 'split', 'style', 'useHTML', 'valueDecimals', 'valuePrefix',
        'valueSuffix', 'xDateFormat'
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)