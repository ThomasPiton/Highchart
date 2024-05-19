from common import Common

class Annotations(Common):
    """
    Represents the annotations options for a Highcharts chart configuration.

    Attributes:
        animation (dict): Animation configuration for the annotations.
        controlPointOptions (dict): Options for the control points of the annotations.
        crop (bool): Whether to crop the annotations.
        draggable (str): The dragging options for the annotations (e.g., 'xy').
        events (dict): Event handlers for the annotations.
        id (str): An ID for the annotations.
        labelOptions (dict): Default options for annotation labels.
        labels (list): An array of label configurations.
        shapeOptions (dict): Default options for annotation shapes.
        shapes (list): An array of shape configurations.
        visible (bool): Visibility of the annotations.
        zIndex (int): The Z-index of the annotations.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'animation', 'controlPointOptions', 'crop', 'draggable', 'events', 
        'id', 'labelOptions', 'labels', 'shapeOptions', 'shapes', 'visible', 
        'zIndex'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Annotations options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)
