# plot_options.py

from chart_component import ChartComponent

class PlotOptions(ChartComponent):

    _valid_attributes = [
        "allowPointSelect","animation","className","colorIndex","colors","connectEnds",
        "connectNulls","cropThreshold","cursor","dashStyle","dataGrouping","dataLabels",
        "depth","enableMouseTracking","exposeElementToA11y","findNearestPointBy","getExtremesFromAll",
        "ignoreHiddenPoint","inactive","index","innerSize","keys","label","linkedTo",
        "minSize","point","pointDescriptionFormatter","pointInterval","pointIntervalUnit",
        "pointPadding","pointPlacement","pointRange","pointStart","pointWidth",
        "selected","shadow","showCheckbox","showInLegend","size","skipKeyboardNavigation",
        "stacking","states","stickyTracking","threshold","tooltip","turboThreshold",
        "visible","zoneAxis","zones"
    ]

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

# ======================================================================================================================

# class PlotOptions:

#     # A list of all valid attributes for the Chart class
#     _valid_attributes = [
#         "allowPointSelect","animation","className","colorIndex","colors","connectEnds",
#         "connectNulls","cropThreshold","cursor","dashStyle","dataGrouping","dataLabels",
#         "depth","enableMouseTracking","exposeElementToA11y","findNearestPointBy","getExtremesFromAll",
#         "ignoreHiddenPoint","inactive","index","innerSize","keys","label","linkedTo",
#         "minSize","point","pointDescriptionFormatter","pointInterval","pointIntervalUnit",
#         "pointPadding","pointPlacement","pointRange","pointStart","pointWidth",
#         "selected","shadow","showCheckbox","showInLegend","size","skipKeyboardNavigation",
#         "stacking","states","stickyTracking","threshold","tooltip","turboThreshold",
#         "visible","zoneAxis","zones"
#     ]

#     def __init__(self, **kwargs):
#         # Initialize all attributes to None or their default values
#         self.__dict__.update({attr: None for attr in self._valid_attributes})
#         # Update the attributes with any values provided upon instantiation
#         self.__dict__.update((k, v) for k, v in kwargs.items() if k in self._valid_attributes)

#     def to_dict(self):
#         """
#         Converts the Chart object into a dictionary suitable for configurations.

#         Returns:
#             dict: A dictionary representing the chart configuration.
#         """
#         return {attr: getattr(self, attr) for attr in self._valid_attributes if getattr(self, attr) is not None}
    
#     @classmethod
#     def from_dict(cls, data):
#         """
#         Creates a Chart object from a dictionary.

#         Parameters:
#             data (dict): A dictionary containing configuration for the chart.

#         Returns:
#             Chart: A Chart object configured according to the provided dictionary.
#         """
#         return cls(**{k: v for k, v in data.items() if k in cls._valid_attributes})
