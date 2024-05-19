from common import Common

class Subtitle(Common):
    """
    Represents the subtitle of the chart, allowing for detailed customization
    of the text, position, style, and other properties.

    Attributes:
        align (str): The horizontal alignment of the subtitle within the chart area.
        floating (bool): Whether the subtitle should be allowed to float.
        margin (int): The margin between the subtitle and the plot area.
        style (dict): CSS styles for the subtitle text.
        text (str): The text content of the subtitle.
        useHTML (bool): Whether HTML is used to render the subtitle's text.
        verticalAlign (str): The vertical alignment of the subtitle within the chart area.
        widthAdjust (int): Adjustment of subtitle width to avoid overlap.
        x (int): The horizontal position of the subtitle relative to the alignment.
        y (int): The vertical position of the subtitle relative to the alignment.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'align', 'floating', 'margin', 'style', 'text', 'useHTML', 'verticalAlign', 'widthAdjust', 'x', 'y'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Subtitle options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
