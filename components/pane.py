from chart_component import ChartComponent

class Pane(ChartComponent):

    _valid_attributes = [
        'background', 'center', 'endAngle', 'size', 'startAngle'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)