# Legend.py

from chart_component import ChartComponent

class Legend(ChartComponent):

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