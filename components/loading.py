from common import Common

class Loading(Common):
    """
    Represents the loading options for a Highcharts chart configuration.

    Attributes:
        hideDuration (int): The duration in milliseconds to hide the loading indicator.
        labelStyle (dict or None): CSS styles for the loading label.
        showDuration (int): The duration in milliseconds to show the loading indicator.
        style (dict or None): CSS styles for the loading indicator.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'hideDuration', 'labelStyle', 'showDuration', 'style'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Loading options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)