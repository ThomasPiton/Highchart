from common import Common

class Pane(Common):
    """
    Represents the pane options for a Highcharts chart configuration.

    Attributes:
        background (list or None): An array of background configurations for the pane.
        center (list): The center of the pane, in percentages or pixel values.
        endAngle (int or None): The end angle of the pane.
        innerSize (str): The inner size of the pane.
        size (str): The size of the pane.
        startAngle (int): The start angle of the pane.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'background', 'center', 'endAngle', 'innerSize', 'size', 'startAngle'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Pane options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)