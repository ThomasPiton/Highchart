from chart_component import ChartComponent

class Annotations(ChartComponent):

    _valid_attributes = [
        "draggable","labelOptions","labels"
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)