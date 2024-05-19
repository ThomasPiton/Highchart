from common import Common

from common import Common

class Credits(Common):
    """
    Represents the credits options for a Highcharts chart configuration.

    Attributes:
        enabled (bool): Whether to show the credits.
        href (str): The URL for the credits link.
        position (dict): The position of the credits.
        style (dict): CSS styles for the credits.
        text (str): The text for the credits.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'enabled', 'href', 'position', 'style', 'text'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Credits options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
