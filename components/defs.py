from common import Common

class Defs(Common):

    _valid_attributes = [
        'glow', 'pattern', 'arrow', 'button', 'marker'
    ]
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)