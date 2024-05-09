from chart_component import ChartComponent

class Colors(ChartComponent):

    _valid_attributes = [
        # This container typically holds an array of color strings.
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)