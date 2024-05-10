# subtitle.py

from common import Common

class Subtitle(Common):
    """
    Represents the subtitle of the chart, allowing for detailed customization
    of the text, position, style, and other properties.

    Attributes:
        text (str): The text content of the title.
        align (str): The horizontal alignment of the title within the chart area.
        margin (int): The margin between the title and the plot area.
        verticalAlign (str): The vertical alignment of the title within the chart area.
        x (int): The horizontal position of the title relative to the alignment.
        y (int): The vertical position of the title relative to the alignment.
        style (dict): CSS styles for the title text.
        floating (bool): Whether the title should be allowed to float.
        useHTML (bool): Whether HTML is used to render the title's text.

    Valid attributes are stored in _valid_attributes list and checked during initialization.
    """
    _valid_attributes = [
        "text","align","margin","verticalAlign","x","y","style","floating","useHTML"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

# ======================================================================================================================

# class Subtitle:

#     _valid_attributes = ["text","align","margin","verticalAlign","x","y","style","floating","useHTML"]

#     def __init__(self, **kwargs):
#         # Initialize all attributes to None or their default values
#         self.__dict__.update({attr: None for attr in self._valid_attributes})
#         # Update the attributes with any values provided upon instantiation
#         self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

#     def to_dict(self):
#         """
#         Converts the Subtitle object into a dictionary suitable for Highcharts configuration.

#         Returns:
#             dict: A dictionary representing the title configuration.
#         """
#         return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}

#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Subtitle object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the title.

#         Returns:
#             Title: A Title object configured according to the provided dictionary.

#         Raises:
#             ValueError: If the required 'text' key is not present in the data.
#         """        
#         return cls(**{k: v for k, v in data.items() if k in cls._valid_attributes})
