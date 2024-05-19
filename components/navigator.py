from common import Common

class Navigator(Common):
    """
    Represents the navigator options for a Highcharts chart configuration.

    Attributes:
        adaptToUpdatedData (bool): Whether to adapt the navigator to updated data.
        annotationsOptions (dict or None): Options for annotations in the navigator.
        baseSeries (int or str or None): The index or ID of the base series for the navigator.
        bindings (dict or None): Bindings for the navigator.
        bindingsClassName (str): CSS class name for the bindings container.
        breadcrumbs (dict or None): Breadcrumbs options for the navigator.
        buttonOptions (dict or None): Options for the navigator buttons.
        enabled (bool): Whether to enable the navigator.
        events (dict or None): Event handlers for the navigator.
        handles (dict or None): Options for the navigator handles.
        height (int or None): The height of the navigator.
        iconsURL (str or None): URL to the icons used in the navigator.
        margin (int or None): The margin for the navigator.
        maskFill (str): The color of the mask fill.
        maskInside (bool): Whether the mask is inside the navigator.
        menuItemHoverStyle (dict or None): CSS styles for menu items on hover.
        menuItemStyle (dict or None): CSS styles for menu items.
        menuStyle (dict or None): CSS styles for the menu.
        opposite (bool): Whether to place the navigator on the opposite side.
        outlineColor (str): The color of the outline.
        outlineWidth (int): The width of the outline.
        series (list or None): Series options for the navigator.
        xAxis (dict or None): X-axis options for the navigator.
        yAxis (dict or None): Y-axis options for the navigator.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'adaptToUpdatedData', 'annotationsOptions', 'baseSeries', 'bindings', 'bindingsClassName',
        'breadcrumbs', 'buttonOptions', 'enabled', 'events', 'handles', 'height', 'iconsURL',
        'margin', 'maskFill', 'maskInside', 'menuItemHoverStyle', 'menuItemStyle', 'menuStyle',
        'opposite', 'outlineColor', 'outlineWidth', 'series', 'xAxis', 'yAxis'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Navigator options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)