from common import Common

class Labels(Common):
    """
    Represents the labels options for a Highcharts chart configuration.

    Attributes:
        items (list or None): An array of label items.
        style (dict or None): CSS styles for the labels.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'items', 'style'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Labels options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)