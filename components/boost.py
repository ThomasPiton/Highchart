from common import Common

from common import Common

class Boost(Common):
    """
    Represents the boost options for a Highcharts chart configuration.

    Attributes:
        allowForce (bool): Whether to allow force boosting.
        debug (dict): Debugging options for the boost module.
        enabled (bool): Whether boosting is enabled.
        pixelRatio (int): Pixel ratio for the boost module.
        seriesThreshold (int): Threshold for the number of series to use boosting.
        useGPUTranslations (bool): Whether to use GPU translations.
        usePreallocated (bool): Whether to use preallocated memory.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'allowForce', 'debug', 'enabled', 'pixelRatio', 'seriesThreshold', 
        'useGPUTranslations', 'usePreallocated'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Boost options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
