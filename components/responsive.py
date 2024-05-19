from common import Common

class Responsive(Common):
    """
    Represents the responsive options in Highcharts, allowing for customization of the chart behavior
    based on different screen sizes and layouts.

    Attributes:
        rules (list or None): A set of rules for responsive behavior.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'rules'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Responsive options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)