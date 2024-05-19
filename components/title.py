# title.py
from common import Common

class Title(Common):
    """
    Represents the title of the chart, allowing for detailed customization
    of the text, position, style, and other properties.

    Attributes:
        align (str): The horizontal alignment of the title within the chart area.
        floating (bool): Whether the title should be allowed to float.
        margin (int): The margin between the title and the plot area.
        style (dict): CSS styles for the title text.
        text (str): The text content of the title.
        useHTML (bool): Whether HTML is used to render the title's text.
        verticalAlign (str): The vertical alignment of the title within the chart area.
        widthAdjust (int): Adjustment of title width to avoid overlap.
        x (int): The horizontal position of the title relative to the alignment.
        y (int): The vertical position of the title relative to the alignment.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'align', 'floating', 'margin', 'style', 'text', 'useHTML', 'verticalAlign', 'widthAdjust', 'x', 'y'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Title options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
