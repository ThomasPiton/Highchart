# title.py
from chart_component import ChartComponent

class Title(ChartComponent):

    _valid_attributes = ["text","align","margin","verticalAlign","x","y","style","floating","useHTML"]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

# ======================================================================================================================

# class Title:
    
#     _valid_attributes = ["text","align","margin","verticalAlign","x","y","style","floating","useHTML"]

#     def __init__(self, **kwargs):
#         # Initialize all attributes to None or their default values
#         self.__dict__.update({attr: None for attr in self._valid_attributes})
#         # Update the attributes with any values provided upon instantiation
#         self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

#     def to_dict(self):
#         """
#         Converts the Title object into a dictionary suitable for Highcharts configuration.

#         Returns:
#             dict: A dictionary representing the title configuration.
#         """
#         return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}

#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Title object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the title.

#         Returns:
#             Title: A Title object configured according to the provided dictionary.
#         """        
#         return cls(**{k: v for k, v in data.items() if k in cls._valid_attributes})
    
    
