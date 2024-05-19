from common import Common

class Drilldown(Common):
    """
    Represents the drilldown options for a Highcharts chart configuration.

    Attributes:
        activeAxisLabelStyle (dict): The style for the active axis label.
        activeDataLabelStyle (dict): The style for the active data label.
        allowPointDrilldown (bool): Whether to allow drilldown on points.
        animation (dict or None): The animation options for drilldown.
        breadcrumbs (dict): The breadcrumb navigation options for drilldown.
        drillUpButton (dict): The configuration options for the drill-up button.
        series (list or None): The series configuration for drilldown.
    """
    
    _list_only = False
    
    _valid_attributes = [
        "activeAxisLabelStyle", "activeDataLabelStyle", "allowPointDrilldown",
        "animation", "breadcrumbs", "drillUpButton", "series"
    ]
    
    _valid_chart = [
        'line', 'bar', 'column', 'area', 'areaspline', 'spline', 
        'pie', 'scatter', 'bubble', 'heatmap', 'boxplot', 'waterfall'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the Drilldown options with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)