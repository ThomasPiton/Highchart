from common import Common

from common import Common

class Caption(Common):
    """
    Represents the caption options for a Highcharts chart configuration.

    Attributes:
        align (str): The horizontal alignment of the caption.
        floating (bool): Whether the caption is floating.
        margin (int): The margin around the caption.
        style (dict): CSS styles for the caption.
        text (str): The text of the caption.
        useHTML (bool): Whether to use HTML to render the caption.
        verticalAlign (str): The vertical alignment of the caption.
        x (int): The x position of the caption.
        y (int or None): The y position of the caption.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'align', 'floating', 'margin', 'style', 'text', 'useHTML', 
        'verticalAlign', 'x', 'y'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Caption options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
