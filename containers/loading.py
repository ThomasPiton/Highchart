from chart_component import ChartComponent

class Loading(ChartComponent):

    _valid_attributes = [
        'hideDuration', 'labelStyle', 'showDuration', 'style'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)