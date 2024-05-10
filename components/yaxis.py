from common import Common

class YAxis(Common):

    _valid_attributes = [
        "allowDecimals","alternateGridColor","categories","ceiling",
        "className","crosshair","dateTimeLabelFormats","endOnTick","events","floor",
        "gridLineColor","gridLineDashStyle","gridLineWidth","gridZIndex","id","labels",
        "lineColor","lineWidth","linkedTo","max","maxLength","min","minPadding","minRange",
        "minTickInterval","minorGridLineColor","minorGridLineDashStyle","minorGridLineWidth",
        "minorTickColor","minorTickInterval","minorTickLength","minorTickPosition","minorTickWidth",
        "offset","opposite","plotBands","plotLines","reversed","showEmpty","showFirstLabel",
        "showLastLabel","startOfWeek","startOnTick","tickAmount","tickColor","tickInterval",
        "tickLength","tickPixelInterval","tickPosition","tickPositioner","tickPositions",
        "tickWidth","tickmarkPlacement","title","type","uniqueNames","units"
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)