# plot_options.py

from common import Common

from common import Common

class PlotOptions(Common):
    """
    Represents the plot options in Highcharts, allowing for detailed customization of the plotting behavior and visual style across different series types.

    Attributes:
        area (dict): Options specific to the area series.
        arearange (dict): Options specific to the area range series.
        areaspline (dict): Options specific to the area spline series.
        areasplinerange (dict): Options specific to the area spline range series.
        bar (dict): Options specific to the bar series.
        bellcurve (dict): Options specific to the bell curve series.
        boxplot (dict): Options specific to the box plot series.
        bubble (dict): Options specific to the bubble series.
        bullet (dict): Options specific to the bullet series.
        column (dict): Options specific to the column series.
        columnpyramid (dict): Options specific to the column pyramid series.
        columnrange (dict): Options specific to the column range series.
        cylinder (dict): Options specific to the cylinder series.
        dependencywheel (dict): Options specific to the dependency wheel series.
        dumbbell (dict): Options specific to the dumbbell series.
        errorbar (dict): Options specific to the error bar series.
        funnel (dict): Options specific to the funnel series.
        funnel3d (dict): Options specific to the funnel 3D series.
        gauge (dict): Options specific to the gauge series.
        heatmap (dict): Options specific to the heatmap series.
        histogram (dict): Options specific to the histogram series.
        item (dict): Options specific to the item series.
        line (dict): Options specific to the line series.
        lollipop (dict): Options specific to the lollipop series.
        networkgraph (dict): Options specific to the network graph series.
        organization (dict): Options specific to the organization series.
        packedbubble (dict): Options specific to the packed bubble series.
        pareto (dict): Options specific to the pareto series.
        pictorial (dict): Options specific to the pictorial series.
        pie (dict): Options specific to the pie series.
        polygon (dict): Options specific to the polygon series.
        pyramid (dict): Options specific to the pyramid series.
        pyramid3d (dict): Options specific to the pyramid 3D series.
        sankey (dict): Options specific to the sankey series.
        scatter (dict): Options specific to the scatter series.
        scatter3d (dict): Options specific to the scatter 3D series.
        series (dict): Options specific to the series.
        solidgauge (dict): Options specific to the solid gauge series.
        spline (dict): Options specific to the spline series.
        streamgraph (dict): Options specific to the stream graph series.
        sunburst (dict): Options specific to the sunburst series.
        tilemap (dict): Options specific to the tilemap series.
        timeline (dict): Options specific to the timeline series.
        treegraph (dict): Options specific to the tree graph series.
        treemap (dict): Options specific to the treemap series.
        variablepie (dict): Options specific to the variable pie series.
        variwide (dict): Options specific to the variwide series.
        vector (dict): Options specific to the vector series.
        venn (dict): Options specific to the venn series.
        waterfall (dict): Options specific to the waterfall series.
        windbarb (dict): Options specific to the wind barb series.
        wordcloud (dict): Options specific to the wordcloud series.
        xrange (dict): Options specific to the xrange series.
    """
    
    _list_only = False
    
    _valid_attributes = [
        'area', 'arearange', 'areaspline', 'areasplinerange', 'bar', 'bellcurve', 'boxplot', 'bubble',
        'bullet', 'column', 'columnpyramid', 'columnrange', 'cylinder', 'dependencywheel', 'dumbbell',
        'errorbar', 'funnel', 'funnel3d', 'gauge', 'heatmap', 'histogram', 'item', 'line', 'lollipop',
        'networkgraph', 'organization', 'packedbubble', 'pareto', 'pictorial', 'pie', 'polygon', 'pyramid',
        'pyramid3d', 'sankey', 'scatter', 'scatter3d', 'series', 'solidgauge', 'spline', 'streamgraph',
        'sunburst', 'tilemap', 'timeline', 'treegraph', 'treemap', 'variablepie', 'variwide', 'vector',
        'venn', 'waterfall', 'windbarb', 'wordcloud', 'xrange'
    ]
    
    def __init__(self, **kwargs):
        """
        Initialize the PlotOptions with given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to the attributes.
        """
        super().__init__(**kwargs)