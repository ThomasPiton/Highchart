from chart_component import ChartComponent

class Labels(ChartComponent):

    _valid_attributes = [
        'items', 'style'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)