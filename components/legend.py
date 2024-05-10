# Legend.py

from common import Common

class Legend(Common):
    """
    Represents the legend of a chart in Highcharts, managing the configuration
    of how series are displayed in the legend. This includes settings for layout,
    style, and interactivity options.

    Attributes:
        align (str): The horizontal alignment of the legend (left, center, or right).
        backgroundColor (str): The background color of the legend.
        borderColor (str): The color of the legend's border.
        borderRadius (int): The border radius of the legend's corners.
        borderWidth (int): The width of the legend's border.
        enabled (bool): Toggles the visibility of the legend.
        floating (bool): Specifies if the legend should float over the chart.
        itemDistance (int): The distance between each item in the legend.
        itemHiddenStyle (dict): Style for the legend items when they are hidden.
        itemHoverStyle (dict): Style for the legend items when hovered.
        itemMarginBottom (int): The margin below each item in the legend.
        itemMarginTop (int): The margin above each item in the legend.
        itemStyle (dict): CSS styles for the legend items.
        itemWidth (int): The width of each item in the legend.
        labelFormat (str): A format string for each legend label.
        layout (str): The layout of the legend items (horizontal or vertical).
        lineHeight (int): The line height between items in the legend.
        margin (int): The margin around the legend.
        maxHeight (int): The maximum height of the legend, after which a scrollbar is added.
        navigation (dict): Options for the navigation of the legend when a scrollbar is present.
        padding (int): The padding inside the legend.
        reversed (bool): Whether to reverse the order of the legend items.
        rtl (bool): Whether the legend items are laid out in a right-to-left order.
        shadow (bool): Whether a shadow is applied to the legend.
        squareSymbol (bool): Whether the symbol next to the text should be square.
        symbolHeight (int): The height of the symbol next to the text.
        symbolPadding (int): The padding between the symbol and the text.
        symbolRadius (int): The border radius of the symbol.
        symbolWidth (int): The width of the symbol next to the text.
        title (dict): An optional title for the legend.
        useHTML (bool): Whether to use HTML to render the text of the legend.
        verticalAlign (str): The vertical alignment of the legend (top, middle, or bottom).
        width (int): The width of the legend.
        x (int): Horizontal offset of the legend from its alignment.
        y (int): Vertical offset of the legend from its vertical alignment.

    Valid attributes are stored in _valid_attributes list and checked during initialization.
    """
    _valid_attributes = [
        "align","backgroundColor","borderColor","borderRadius","borderWidth","enabled","floating",
        "itemDistance","itemHiddenStyle","itemHoverStyle","itemMarginBottom","itemMarginTop",
        "itemStyle","itemWidth","labelFormat","layout","lineHeight","margin","maxHeight",
        "navigation","padding","reversed","rtl","shadow","squareSymbol","symbolHeight",
        "symbolPadding","symbolRadius","symbolWidth","title","useHTML","verticalAlign",
        "width","x", "y"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)




# ======================================================================================================================


# class Legend:

#     _valid_attributes = [
#         "align","backgroundColor","borderColor","borderRadius","borderWidth","enabled","floating",
#         "itemDistance","itemHiddenStyle","itemHoverStyle","itemMarginBottom","itemMarginTop",
#         "itemStyle","itemWidth","labelFormat","layout","lineHeight","margin","maxHeight",
#         "navigation","padding","reversed","rtl","shadow","squareSymbol","symbolHeight",
#         "symbolPadding","symbolRadius","symbolWidth","title","useHTML","verticalAlign",
#         "width","x", "y"
#     ]

#     def __init__(self, **kwargs):
#         # Initialize all attributes to None or their default values
#         self.__dict__.update({attr: None for attr in self._valid_attributes})
#         # Update the attributes with any values provided upon instantiation
#         self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

#     def to_dict(self):
#         """
#         Converts the Legend object into a dictionary suitable for configurations.

#         Returns:
#             dict: A dictionary representing the Legend configuration.
#         """
#         return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}
    
#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Legend object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the Legend.

#         Returns:
#             Legend: A Legend object configured according to the provided dictionary.
#         """
#         # Filter the dictionary to only include keys that are valid attributes
#         return cls(**{k: v for k, v in data.items() if k in cls._valid_attributes})