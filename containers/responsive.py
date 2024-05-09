from chart_component import ChartComponent

class Scrollbar(ChartComponent):

    _valid_attributes = [
        'rules'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)