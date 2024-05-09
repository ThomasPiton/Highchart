from chart_component import ChartComponent

class Navigator(ChartComponent):

    _valid_attributes = [
        'adaptToUpdatedData', 'baseSeries', 'enabled', 'handles', 'height',
        'margin', 'maskFill', 'maskInside', 'opposite', 'outlineColor',
        'outlineWidth', 'series', 'xAxis', 'yAxis'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)