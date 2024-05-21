# accessibility.py

from common import Common

class Accessibility(Common):
    """
    Represents the accessibility options for a Highcharts chart configuration.

    Attributes:
        announceNewData (dict): Configuration for announcing new data.
        customComponents (dict): Custom components for accessibility.
        description (str): Description of the chart for screen readers.
        enabled (bool): Whether accessibility options are enabled.
        highContrastMode (str): Mode for high contrast, can be 'auto'.
        highContrastTheme (dict): Theme configuration for high contrast mode.
        keyboardNavigation (dict): Configuration for keyboard navigation.
        landmarkVerbosity (str): Level of verbosity for landmarks.
        linkedDescription (str): CSS selector for a linked description element.
        linkDate (str): Description linking date information.
        point (dict): Accessibility options for data points.
        screenReaderSection (dict): Configuration for screen reader section.
        series (dict): Accessibility options for series.
        typeDescription (str): Type description of the chart for screen readers.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'announceNewData', 'customComponents', 'description', 'enabled', 
        'highContrastMode', 'highContrastTheme', 'keyboardNavigation', 
        'landmarkVerbosity', 'linkedDescription', 'linkDate', 'point', 
        'screenReaderSection', 'series', 'typeDescription'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Accessibility options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
