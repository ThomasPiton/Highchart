from common import Common

class Pane(Common):

    _valid_attributes = [
        'background', 'center', 'endAngle', 'startAngle','size', 'innerSize',
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)