from chart_component import ChartComponent

class Defs(ChartComponent):

    _valid_attributes = [
        'glow', 'pattern', 'arrow', 'button', 'marker'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)