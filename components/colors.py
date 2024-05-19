from common import Common

class Colors(Common):
    """
    Represents the colors options for a Highcharts chart configuration.

    Attributes:
        None
    """
    
    _list_only = True
    
    _valid_attributes = []
    
    def __init__(self, values=None):
        """
        Initialize the Colors options with given list of values.

        Args:
            values (list): A list of color values to be used in the chart.
        """
        super().__init__(values=values or [])