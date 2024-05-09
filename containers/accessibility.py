from chart_component import ChartComponent

class Accessibility(ChartComponent):

    _valid_attributes = [
        'enabled', 'screenReaderSection', 'description', 'typeDescription', 'keyboardNavigation',
        'point', 'series', 'landmarkVerbosity', 'linkDate', 'announceNewData'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)